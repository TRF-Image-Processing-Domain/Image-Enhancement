import numpy as np
import cv2

input=cv2.imread('Images/1.jpg')
matrix_size=3    #size of matrix we will be sliding over image calculating alpha beta in repeatedly
y_len,x_len,channel=input.shape
new_img = np.zeros(input.shape, input.dtype)  #create new image with same shape as of input, later will be using it to append the new image parts to get whole image

for ey in range(0,y_len-matrix_size):
    for ex in range(0,x_len-matrix_size):
        img=input[ey:ey+matrix_size,ex:ex+matrix_size] #slicing image into specified matrix
        #calculating alpha and beta for this specified region
        amean = img.mean()
        if amean == 0:
            amean = 1
        alpha = (255 / (amean))
        if alpha > 3:
            alpha = 3
        #print('alpha: ', alpha)
        beta = (amean / (alpha))
        #print('beta: ', beta)
        new_img[ey:ey+matrix_size,ex:ex+matrix_size]=cv2.convertScaleAbs(img, alpha=alpha,beta=beta) # appending operated image parts into that image we created before
cv2.imshow("Input",input)
cv2.imshow("Output",new_img)
#result = np.concatenate((input, new_img), axis=1)
#cv2.imwrite('BasicLinearTransforamtion_byParts_4.jpg',result )
cv2.waitKey()
