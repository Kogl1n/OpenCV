# Structural similarity index to produce nice timelapse images

# Install:
# conda install -c menpo opencv ffmpeg scikit-image
# Rendering the timelapse video:
# ffmpeg -r 1 -i folder/%04d.png -c:v libx264 -vf "fps=50,setpts=0.25*PTS" -pix_fmt yuv420p out.mp4

# situation: A 3D printer moves from left to right and adds layers in the z-direction.
# idea: The image similarity goes down exponentially and returns exponentially when the printer head returns.
#       So, basically there a two very similar positions: Right after the last image and when returning.
#       With the left-right-return motion e.g. lasting for two seconds, we have with 25fps a total of 50 images to compare
#       similarity to. Even if the the intervall windows is not 100% correct, since we have two ideal points it does not matter
#       much.
#       Another way would be to glue a blob of a specific (rare) color to the printer head and perform a blob detection regarding a
#       defined region of interest (ROI). (If NOSNAPYET AND x in ROI AND x>mean(x_last, x_2last) a.k.a. head returns moving right
#       then take a snapshot and set NOSNAPYET=0) Be aware of the different naming of the function call between OpenCV 2 and 3.

import numpy as np
import cv2
from skimage.measure import compare_ssim as ssim
import time

intervall = 2                               # seconds the head needs to return
number = 25*intervall

cap = cv2.VideoCapture(0)
ret,previous = cap.read()

best_frame = previous                       # initial image

file = 0
 
while(True):
    i = 0
    best_s = 0
    while(i<=number):
        i += 1
        ret, frame = cap.read()
        s = ssim(frame, previous, multichannel=True)
        if(s > best_s):
            best_s = s
            best_frame = frame
    cv2.imwrite('folder/%04d.png' % file,best_frame)
    file += 1
    previous = best_frame
 
cap.release()
cv2.destroyAllWindows()
