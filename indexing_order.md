# OpenCV: Things to remember

## colors: 
BGR instead of RGB, but CV_RGB(r, g, b)  

## shape:
height:	image.shape[0]  
width: 	image.shape[1]  
colors:	image.shape[2]  

## matrix access
start: upper left (0,0)  
crop: image[0:100, 0:100] # y,x, excluding 100 like range(0, 100, 25)  
draw: cv2.line(canvas, (300, 0), (0, 300), red, 3) # x,y top right to bottom left  

## shift
M1 = np.float32([[1, 0, 25], [0, 1, 50]]) # x,y  
shifted_down = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))  

## rotate
counter-clockwise a.k.a. mathematical sense  

## flip
flipped = cv2.flip(image, 1) # flipped horizontally/flipped at horizontal line   
flipped = cv2.flip(image, 0) # flipped vertically/flipped at vertical line   
flipped = cv2.flip(image, -1) # flipped vertically + horizontally  

## resize
dim1 = (150, int(image.shape[0] * ratio1)) # new (w, h) dimensions  
resized_width = cv2.resize(image, dim1, interpolation = cv2.INTER_AREA) # (w,h)  

## Sobel gradient
sobelX = cv2.Sobel(img,cv2.CV_64F,1,0) # along the x-axis (finding vertical edges)  
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1) # along the y-axis (finding horizontal edges)  
 
## Canny edge
(blur, Sobel gradient x,y, supressing edges, hysteresis thresholding) 
canny = cv2.Canny(image, 30, 150) # two thresholds  

## Contours
cv2.findContours: destructive to input  
OpenCV 3: 3-tuple  
OpenCV 2.4: 2-tuple  
