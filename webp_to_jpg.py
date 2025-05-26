import os
import threading
from tkinter import *
from tkinter import ttk, filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image

class WebPConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("WebP → JPG/PNG 변환기")
        self.master.configure(bg="#f7f7f7")
        self.master.resizable(False, False)

        # 상태 변수
        self.source_folder = StringVar()
        self.format = StringVar(value='jpg')

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("TLabel", background="#f7f7f7", font=("Segoe UI", 10))

        Label(master, text="📂 변환할 WebP 폴더 선택 또는 드래그:", font=("Segoe UI", 11, "bold")).pack(pady=(10, 4))

        self.drop_area = Label(master, text="🗂 여기에 폴더 끌어다 놓기", relief="solid", borderwidth=1, width=40, height=2,
                               bg="white", font=("Segoe UI", 10))
        self.drop_area.pack(pady=4)
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.handle_drop)

        ttk.Button(master, text="폴더 선택", command=self.browse_folder).pack(pady=5)

        Label(master, text="📷 저장 형식 선택:").pack(pady=(10, 2))
        format_frame = Frame(master, bg="#f7f7f7")
        format_frame.pack()
        Radiobutton(format_frame, text="JPG", variable=self.format, value='jpg', bg="#f7f7f7").pack(side=LEFT, padx=10)
        Radiobutton(format_frame, text="PNG", variable=self.format, value='png', bg="#f7f7f7").pack(side=LEFT, padx=10)

        ttk.Button(master, text="▶ 변환 시작", command=self.start_conversion).pack(pady=12)

        self.progress = ttk.Progressbar(master, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(pady=4)

        self.status = Label(master, text="", fg="#555")
        self.status.pack(pady=(2, 10))

    def handle_drop(self, event):
        folder = event.data.strip('{}')
        if os.path.isdir(folder):
            self.source_folder.set(folder)
            self.drop_area.config(text=f"✅ 선택됨:\n{folder}")

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.source_folder.set(folder)
            self.drop_area.config(text=f"✅ 선택됨:\n{folder}")

    def start_conversion(self):
        if not self.source_folder.get():
            self.status.config(text="⚠️ 변환할 폴더를 선택하세요.")
            return

        t = threading.Thread(target=self.convert_images)
        t.start()

    def convert_images(self):
        src = self.source_folder.get()
        fmt = self.format.get()
        converted_count = 0

        files = []
        for dirpath, _, filenames in os.walk(src):
            for f in filenames:
                if f.lower().endswith('.webp'):
                    files.append(os.path.join(dirpath, f))

        total = len(files)
        self.progress['maximum'] = total

        for i, webp_path in enumerate(files):
            try:
                output_path = os.path.splitext(webp_path)[0] + '.' + fmt
                with Image.open(webp_path) as img:
                    format_str = 'JPEG' if fmt.lower() == 'jpg' else fmt.upper()
                    img.convert("RGB").save(output_path, format_str)

                os.remove(webp_path)
                converted_count += 1

                self.progress['value'] = i + 1
                self.status.config(text=f"🔄 {i+1}/{total} 변환 중...")
                self.master.update_idletasks()

            except Exception as e:
                print(f"오류: {webp_path}: {e}")

        self.status.config(text=f"🎉 총 {converted_count}개 변환 완료!")
        self.progress['value'] = 0


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = WebPConverterApp(root)
    root.geometry("420x380")
    root.mainloop()
