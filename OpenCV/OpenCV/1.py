# import cv2
# image = cv2.imread("car_img.jpg")
# h,w = image.shape[:2]
# print(f"height: {h}, width: {w}")

import cv2

# Load an image
img = cv2.imread("car_img.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur image -> makes image clearer when detecting -> smooth the image
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Edge detection
edges = cv2.Canny(blur, 50, 150)

# Show results 
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Blurred", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
