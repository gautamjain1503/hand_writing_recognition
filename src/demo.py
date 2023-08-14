from predict import get_img_text
import cv2
img=cv2.imread("../test/3.png")
img,text=get_img_text(img)
cv2.imwrite("11.jpg",img)

print(text)

cv2.namedWindow(text, cv2.WINDOW_NORMAL)

cv2.resizeWindow(text, 500, 700)

cv2.imshow(text,img)

cv2.waitKey(0)