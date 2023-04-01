import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("image.jpg")

img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(img_gray, scaleFactor=1.05, minNeighbors=5)
print(type(faces))
print(faces)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)

resized=cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Image with Face Recognition!", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
