import cv2
import numpy as np

temp = cv2.imread("Images/1.jpg")
img = cv2.resize(temp,(600,400))

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
equ_v=cv2.equalizeHist(v)
final=cv2.merge((h,s,equ_v))
new_img=cv2.cvtColor(final,cv2.COLOR_HSV2BGR)
cv2.imshow("Input",img)
cv2.imshow("Output",new_img)
#result = np.concatenate((img, new_img), axis=1)
#cv2.imwrite('HistogramEqualization_UsingHSV_4.jpg',result )
cv2.waitKey()
