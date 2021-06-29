import cv2
import numpy as np

image = cv2.imread("download.jfif")
img = cv2.resize(image,(750,600))

#edges-1
#blurred_img = cv2.medianBlur(img,5)
#edges  = cv2.Canny(blurred_img,75,150)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

#color-2
color = cv2.bilateralFilter(img,9,300,300)

#cartoon - 3
cartoon = cv2.bitwise_and(color,color,mask=edges)

cv2.imshow("Image",img)
cv2.imshow("cartoon",cartoon)
# cv2.imshow("color",color)
# cv2.imshow("edges",edges)
#cv2.imshow("gray",gray)
# cv2.imshow("edges",edges)
# cv2.imshow("color",color)
cv2.waitKey(0)
cv2.destroyAllWindows()