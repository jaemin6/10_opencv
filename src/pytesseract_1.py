#import easyocr
import pytesseract
import cv2
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#reader = easyocr.Reader(['ch_tra', 'en'], gpu=False)
img_path = '../img/chinese_tra.jpg'
img = cv2.imread(img_path)
# 1. 이미지 불러오기 
#plt.figure(figsize=(7,8))
#plt.imshow(cv1.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()
print("\n=== 중국어 인식 테스트 ===")
try:
    text_chi = pytesseract.image_to_string(img_path, lang='chi_tra')
    print("중국어 결과:", repr(text_chi))
except Exception as e:
    print(f"중국어 인식 실패: {e}")

# 2. 영어로 먼저 테스트
print("\n=== 영어 인식 테스트 ===")
try:
    text_eng = pytesseract.image_to_string(img_path, lang='eng')
    print("영어 결과:", repr(text_eng))
except Exception as e:
    print(f"영어 인식 실패: {e}")

# 2. 이미지 텍스트 인식 
#result = reader.readtext(img_path)
#print(result)
#data = pytesseract.image_to_data(img_path, lang='chi_tra+eng', output_type=pytesseract.Output.DICT)
#print(data)
# 3. 인식된 텍스트 확인해보기 

#THRESHOLD = 0.5

#for bbox, text, conf in result:
#    if conf >= THRESHOLD:
#        print(text)
#        cv2.rectangle(img, pt1=bbox[0], pt2=bbox[2], color=(0, 255, 0), thickness=2)
#    plt.figure(figsize=(8,8))
#    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#    plt.axis('off')
#    plt.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()