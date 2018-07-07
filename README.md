# OpenCV
(examples work also for OpenCV 3.0 and Python 3+)  
June 2015, OpenCV 3.0, OpenCL support, Python 3 support!  

# Useful packages  
$ pip install numpy  
$ pip install scipy  
$ pip install matplotlib  

$ pip install mahotas			# mahotas complements OpenCV  
$ pip install scikit-learn   
$ pip install -U scikit-image	# state of the art algos: scikit-image  
$ pip install menpo # importing, manipulating and visualizing image and mesh data   

# Install
Full install ~3GB but python3-OpenCV is actually enough.  

## Windows
Install numpy, scipy and matplotlib first.  
pip install C:/some-dir/opencv-file.whl from  
https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
Then:  
pip install --upgrade pip (if Python script dir is in PATH var)  

## Linux
(apt-get install python3-pip)  
pip install numpy or apt-get install python3-numpy.  
pip install matplotlib or apt-get install python3-matplotlib.
apt-get install python3-OpenCV

# FFmpgeg
## Installing FFmpeg on Windows
Download FFmpeg from https://ffmpeg.zeranoe.com/builds/  
Unpack the zip file   
Open a command prompt (with admin rights) and execute setx /M PATH "path\to\ffmpeg\bin;%PATH%"  
OR add the path manually to your PATH variable  

## Installing FFmpeg on Ubuntu
sudo add-apt-repository ppa:mc3man/trusty-media  
sudo apt-get update  
sudo apt-get install ffmpeg  
sudo apt-get install frei0r-plugins  

# Dlib 
face detection, facial landmarks, correlation tracking, etc.
## install 
$ sudo apt-get update
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libopenblas-dev liblapack-dev 
$ sudo apt-get install libx11-dev libgtk-3-dev
$ sudo apt-get install python python-dev python-pip
$ sudo apt-get install python3 python3-dev python3-pip

$ mkvirtualenv dlib_test -p python3
$ workon cv
$ pip install numpy # may be called pip3 for python3
$ pip install dlib

>>> import dlib # version check
>>> dlib.__version__

## Face Recognition
face_recognition package utilizing dlib :  
https://github.com/ageitgey/face_recognition#python-code-examples  



