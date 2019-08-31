import cv2
import numpy as np
import imutils

image = cv2.imread('images.jpg')
cv2.waitKey(0)
print(image.shape)
x = image.shape[0]
y = image.shape[1]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
cv2.circle(image, (97,65),5, (255, 0, 255), -1)


	# show the image
cv2.imshow("Image", image)
print(cX,cY)
cv2.waitKey(0)
