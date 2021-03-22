import cv2

img = cv2.imread("Gravatar.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("gray.png", gray_img)
inverted_img = (255 - gray_img)
#cv2.imwrite("inv.png", inverted_img)
blurred = cv2.GaussianBlur(inverted_img, (21, 21), 0)
#cv2.imwrite("blur.png", blurred)
inverted_blurred = 255 - blurred
#cv2.imwrite("invblur.png", inverted_blurred)
pencil_sketch = cv2.divide(gray_img, inverted_blurred, scale=256.0)
cv2.imwrite("sketch.png", pencil_sketch)
