import cv2
import numpy as np

img = cv2.imread("Images/1.jpg")
b,g,r=cv2.split(img)
equb = cv2.equalizeHist(b)
equg = cv2.equalizeHist(g)
equr = cv2.equalizeHist(r)
equ = cv2.merge((equb,equg,equr))
cv2.imshow("Input",img)
cv2.imshow("Output",equ)
result = np.concatenate((img, equ), axis=1) #combining images
cv2.imwrite('HistogramEqualization_RGB_4.jpg',result )
cv2.waitKey()
