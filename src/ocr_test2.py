import easyocr
import cv2
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 1. 한글 폰트 설정 (Windows 기준: 말굿체)
font_path = "C:/Windows/Fonts/malgun.ttf"  # 나눔고딕도 가능
fontprop = fm.FontProperties(fname=font_path, size=12)
plt.rc('font', family=fontprop.get_name())

# 2. EasyOCR 리더 생성
reader = easyocr.Reader(['ko', 'en'], gpu=False)

# 3. 이미지 로드
img_path = '../img/sign.jpg'  # 교통 표지판 이미지 경로
img = cv2.imread(img_path)

# 4. 텍스트 인식
results = reader.readtext(img)

# 5. 이미지 시각화 준비
plt.figure(figsize=(12, 12))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# 6. 결과 표시 (matplotlib으로 텍스트 출력)
for bbox, text, conf in results:
    if conf >= 0.5:
        # 바운딩 박스 좌표
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))

        # 사각형 박스 그리기
        plt.plot(
            [top_left[0], top_right[0], bottom_right[0], bottom_left[0], top_left[0]],
            [top_left[1], top_right[1], bottom_right[1], bottom_left[1], top_left[1]],
            color='lime', linewidth=2
        )

        # 텍스트와 정확도 표시
        plt.text(top_left[0], top_left[1] - 10,
                 f'{text} ({conf:.2f})',
                 color='red', fontsize=12, fontproperties=fontprop)

# 7. 출력
plt.axis('off')
plt.title('OCR 결과', fontproperties=fontprop)
plt.show()
