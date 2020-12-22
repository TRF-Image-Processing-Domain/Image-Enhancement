import cv2
import numpy as np

def adjust_gamma(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")  # created table where we are scaling our image pixel intensities from the range [0, 255] to [0, 1.0]
                                                    #and ** invGamma as Output intensity= Input intensity ^ (1 / G)
    return cv2.LUT(image, table)
x = 'Images/1.JPG'  #location of the image
original = cv2.imread(x, 1)
cv2.imshow('original',original)
def empty(a):
    pass
low_k=1
high_k=400
cv2.namedWindow('slider')
cv2.resizeWindow('slider',500,100)
gamma1='gamma'
cv2.createTrackbar('gamma1','slider',low_k,high_k,empty) #creating trackbar with range of 400 value
while (True):
    temp=cv2.getTrackbarPos('gamma1','slider')
    gamma2=temp/100  #receiving gamma withiin range of 0.01 to 4
    adjusted = adjust_gamma(original,gamma2) #calling the main funciotn
    cv2.putText(adjusted, "g={}".format(gamma2), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("gammam image 1", adjusted) # showing output
    k=cv2.waitKey(1)
    if k == ord(' '):
        break
cv2.destroyAllWindows()
