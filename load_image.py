# Load a png image, print shape info, show and save the image as jpg  
# $ python load_image.py --image ../images/image.png  

from __future__ import print_function  
import argparse 											                # parse command line arguments
import cv2  

ap = argparse.ArgumentParser()						
ap.add_argument("-i", "--image", required = True,			# --image path to image
help = "Path to the image")  
args = vars(ap.parse_args())  
image = cv2.imread(args["image"])							        # Numpy array
print("width: {} pixels".format(image.shape[1]))			# shape: height, width, colors
print("height: {} pixels".format(image.shape[0]))  
print("channels: {}".format(image.shape[2]))  

cv2.imshow("Image", image)								            # show image
cv2.waitKey(0)											                  # anykey
cv2.imwrite("newimage.jpg", image)						        # save as jpg

