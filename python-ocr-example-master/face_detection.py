# load the library using the import keyword
# OpenCV must be properly installed for this to work. If not, then the module will not load with an
# error message.

import cv2
import sys
import os
# Gets the name of the image file (filename) from sys.argv
class MyImage:
    def __init__(self, img_name):
        self.img = cv2.imread(img_name)
        self.__name = img_name

    def __str__(self):
        return self.__name

name = str(sys.argv[1])
cascPath = "haarcascade_frontalface_default.xml"

# This creates the cascade classifcation from file 

faceCascade = cv2.CascadeClassifier(cascPath)

# The image is read and converted to grayscale
image = cv2.imread(name)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# The face or faces in an image are detected
# This section requires the most adjustments to get accuracy on face being detected.


faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=7,
    minSize=(1, 1),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Detected {0} faces!".format(len(faces)))

# This draws a green rectangle around the faces detected
cropped = image
padding = 20
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x-padding, y-padding*4), (x+w+padding, y+h+padding), (0, 255, 0), 2)
    cropped = image[ y-padding*4:y+h+padding, x-padding:x+w+padding]
path = '/home/elwess/Desktop/nodeVision/public/uploads'
img_name = name.split("/uploads/", 1)
cv2.imwrite(os.path.join(path, 'face'+img_name[1]), cropped)
print(img_name[1])
print('done')