import cv2

# configurable parameters
source = "myimage.jpg"
destination = "newMyimage.jpg"
scale_percent = 50  # PERCENT BY WHICH IMAGE IS RESIZED

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)


# CALCULATE THE 50 PERCENT OF ORIGINAL DIMENSIONS
new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)

dsize = (new_width, new_height)   # TUPLE

# RESIZE IMAGE
output = cv2.resize(src, dsize)
cv2.imwrite(destination, output)

cv2.waitKey(0)