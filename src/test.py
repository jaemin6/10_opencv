import pytesseract
import cv2
import matplotlib.pyplot as plt
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_path = '../img/chinese_tra.jpg'

print("=== 기본 진단 ===")

# 1. 이미지 파일 존재 확인
if os.path.exists(img_path):
    print("✅ 이미지 파일 존재")
else:
    print("❌ 이미지 파일 없음:", img_path)
    print("현재 디렉토리:", os.getcwd())
    print("상위 폴더 내용:", os.listdir('../') if os.path.exists('../') else "상위 폴더 없음")
    exit()

# 2. 이미지 로드 확인
img = cv2.imread(img_path)
if img is not None:
    print(f"✅ 이미지 로드 성공: {img.shape}")
else:
    print("❌ 이미지 로드 실패")
    exit()

# 3. Tesseract 설치 확인
try:
    version = pytesseract.get_tesseract_version()
    print(f"✅ Tesseract 버전: {version}")
except Exception as e:
    print(f"❌ Tesseract 실행 실패: {e}")
    exit()

# 4. 언어팩 확인
try:
    languages = pytesseract.get_languages()
    print(f"✅ 설치된 언어: {languages}")
except Exception as e:
    print(f"❌ 언어 확인 실패: {e}")

# 5. 이미지 표시
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title(f'Image: {img_path}')
plt.axis('off')
plt.show()

# 6. 간단한 텍스트로 먼저 테스트 (Tesseract 자체 테스트)
print("\n=== Tesseract 자체 테스트 ===")
try:
    # 간단한 흑백 텍스트 이미지 생성
    import numpy as np
    test_img = np.ones((100, 300, 3), dtype=np.uint8) * 255
    cv2.putText(test_img, 'Hello World', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    test_result = pytesseract.image_to_string(test_img, lang='eng')
    print(f"테스트 결과: '{test_result.strip()}'")
    
    if 'Hello' in test_result:
        print("✅ Tesseract 정상 작동")
    else:
        print("❌ Tesseract 문제 있음")
        
except Exception as e:
    print(f"❌ 테스트 실패: {e}")

# 7. 원본 이미지로 다시 테스트
print("\n=== 원본 이미지 테스트 ===")
try:
    # 설정 변경해가며 테스트
    configs = [
        '--psm 6',  # 단일 텍스트 블록
        '--psm 8',  # 단일 단어
        '--psm 13', # 원시 라인
        '--psm 3'   # 자동 페이지 분할
    ]
    
    for config in configs:
        try:
            text = pytesseract.image_to_string(img_path, lang='eng', config=config)
            print(f"PSM {config}: '{text.strip()[:50]}...'")
        except Exception as e:
            print(f"PSM {config} 실패: {e}")
            
except Exception as e:
    print(f"❌ 원본 이미지 테스트 실패: {e}"