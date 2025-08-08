
# easyocr 활용한 교통 표지판 읽기 결과
```
# 1. 한글 폰트 설정 (Windows 기준: 말굿체)
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글을 못읽고 ??????? 로 표기되어 폰트를 추가함
fontprop = fm.FontProperties(fname=font_path, size=12)
plt.rc('font', family=fontprop.get_name())  
# => matplotlib에서 한글 폰트 사용하도록 설정

# 2. EasyOCR 리더 생성
reader = easyocr.Reader(['ko', 'en'], gpu=False)  
# => 한국어, 영어 지원하는 OCR 리더 생성, GPU는 사용 안 함

# 3. 이미지 로드
img_path = '../img/sign.jpg'  # 교통 표지판 이미지 경로
img = cv2.imread(img_path)  
# => OpenCV로 이미지 파일 읽기 (BGR 형식)

# 4. 텍스트 인식
results = reader.readtext(img)  
# => EasyOCR로 이미지 내 텍스트 인식 실행
# 결과는 리스트, 각 원소는 [바운딩박스, 텍스트, 신뢰도]

# 5. 이미지 시각화 준비
plt.figure(figsize=(12, 12))  
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  
# => matplotlib로 이미지를 RGB 형식으로 변환해 보여줄 준비

# 6. 결과 표시 (matplotlib으로 텍스트 출력)
for bbox, text, conf in results:
    if conf >= 0.5:  
        # 신뢰도가 50% 이상인 결과만 처리
        
        # 바운딩 박스 좌표 (4점)
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))  
        bottom_right = tuple(map(int, bottom_right))
        # => 좌표 값을 정수형 튜플로 변환 (픽셀 좌표)

        # 사각형 박스 그리기 (인식된 글자 영역 표시)
        plt.plot(
            [top_left[0], top_right[0], bottom_right[0], bottom_left[0], top_left[0]],
            [top_left[1], top_right[1], bottom_right[1], bottom_left[1], top_left[1]],
            color='lime', linewidth=2
        )

        # 텍스트와 정확도 표시 (이미지 위에 텍스트 출력)
        plt.text(top_left[0], top_left[1] - 10,
                 f'{text} ({conf:.2f})',  # 인식된 글자 + 정확도 소수점 2자리
                 color='red', fontsize=12, fontproperties=fontprop)

        # 터미널(콘솔)에도 텍스트와 정확도 출력
        print(f"텍스트: {text}, 정확도: {conf:.2f}")

# 7. 출력
plt.axis('off')  
# => 이미지 축 눈금 제거

plt.title('OCR 결과', fontproperties=fontprop)  
# => 그래프 제목 한글 폰트로 표시

plt.show()  
# => 이미지와 그 위에 그린 박스, 텍스트를 화면에 보여줌
```
<img width="604" height="868" alt="image" src="https://github.com/user-attachments/assets/e4a86c48-9c8d-4085-98bf-f4301cbe336e" />

## print(f"텍스트: {text}, 정확도: {conf:.2f}")
print문으로 콘솔에 텍스트와 정확도를 표시하게 나타냄
<img width="302" height="91" alt="image" src="https://github.com/user-attachments/assets/9f0b4d5d-23e0-4c1f-a02c-d0c075a77a7a" />
