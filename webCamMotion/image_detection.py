import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("image.jpg")

#creating a gray copy of the image for better detection
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#setting the rate of scaling (5%) for the picture (building the image pyramid -> regardless of the face's size, it will get recognized by the algorithm, provided
# the scaleFactor is a decent one
faces=face_cascade.detectMultiScale(img_gray, scaleFactor=1.05, minNeighbors=5)
print(type(faces))
print(faces)

for x, y, w, h in faces:
    # iterating over the faces list with (x,y) being the left-top corner of the rectangle and w,h = weight, height
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)

#resizing my quite large picture (update: the cropped one is better, optional resizing)
resized=cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Image with Face Recognition!", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
