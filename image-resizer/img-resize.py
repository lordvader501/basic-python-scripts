import cv2 as cv
import os

# Taking user input of path and checking that path exist or not.
while True:
    path = input("Input image name >>> ")
    if path == "QUIT":
        break
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),"images",path)):
        img = cv.imread(os.path.join(os.path.dirname(os.path.abspath(__file__)),"images",path))
        break
    else:
        print("File not found.")
        
height = int(input("enter Height: "))
width = int(input("enter Width: "))
dim = (height, width)

resized_img = cv.resize(img, (height,width), interpolation= cv.INTER_AREA)

path2 = input("enter file name to save: ")
cv.imwrite(os.path.join(os.path.dirname(os.path.abspath(__file__)),"results",f"{path2}.jpg"), resized_img)

cv.destroyAllWindows()