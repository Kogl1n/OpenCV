# Blob detection

import cv2
import numpy as np
 
im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)
 
params = cv2.SimpleBlobDetector_Params()
 
params.minThreshold = 20 # Threshold
params.maxThreshold = 200

params.filterByArea = True # Area
params.minArea = 1000
 
params.filterByCircularity = True # Circularity
params.minCircularity = 0.1
 
params.filterByConvexity = True # Convexity
params.minConvexity = 0.85

params.filterByInertia = True # Inertia
params.minInertiaRatio = 0.01
 
# depending of version
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(im) # only works with data type of uint8 
 
# Draw detected blobs as red circles with same size
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
