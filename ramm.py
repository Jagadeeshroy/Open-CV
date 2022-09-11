import cv2

img = cv2.imread('ramcharan.jpg',1)
#print(img)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

