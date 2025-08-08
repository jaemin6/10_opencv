import easyocr
import cv2
import matplotlib.pyplot as plt

reader = easyocr.Reader(['ch_tra', 'en'], gpu=False)
result = reader.readtext('ch_tr.jpg')

img = cv2.imread('ch_tr.jpg')
result = reader.readtext(img)

plt.figure(figsize=(8, 8))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
