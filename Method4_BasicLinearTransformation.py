import cv2
import numpy as np

def autoAdjustments(img):
    amean = img.mean()  #average intensity of all the pixels
    #print(amean)
    if amean==0:
        amean=1
    alpha = (255 / (amean)) #aiming to get alpha value between (1 to 3),corresponds to contrast
    if alpha>3:
        alpha=3
    print('alpha: ',alpha)
    beta = (amean/(alpha)) #beta corresponds to brightness parameter, aiming to get value approx 30-60,
                    # constant val by which each pixel value will increment)
    print('beta: ',beta)
    new_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)#performs new_intensity = old_intensity*alpha + beta on every pixel

    cv2.imshow("Intput", input)
    cv2.imshow("Output", new_img)
    #result = np.concatenate((input, new_img), axis=1) #combining images
    #cv2.imwrite('BasicLinearTransformation_1.jpg',result )
    cv2.waitKey()

input = cv2.imread("Images/1.jpg")
#new_img = np.zeros(input.shape, input.dtype)
autoAdjustments(input)

