# WebP → JPG/PNG 변환기 (Windows GUI)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-lightgrey)
![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-orange)

## 📌 소개

이 프로그램은 Windows 환경에서 `.webp` 이미지를 **JPG** 또는 **PNG**로 일괄 변환하는 GUI 도구입니다.  
폴더를 선택하거나 끌어다 놓기만 하면 변환이 시작되며, 변환된 파일은 **같은 폴더**에 저장되고 원본 **.webp** 파일은 삭제됩니다.

## 🎨 주요 기능

- ✅ `.webp` → **JPG/PNG** 일괄 변환  
- ✅ **드래그 앤 드롭**(폴더) 지원  
- ✅ **진행률 표시** 및 상태 메시지  
- ✅ **원본 파일 자동 삭제**

## 🖼️ 스크린샷

> ![앱 실행 화면 예시](screenshot.png)  
> 1) 폴더 선택/드래그 → 2) 형식 선택 → 3) 변환 시작

## 💡 설치 및 실행 방법

### 1. 소스 실행 (Python 필요)

1. Python 3.8 이상 설치  
2. 라이브러리 설치:
   ```bash
   pip install pillow tkinterdnd2
