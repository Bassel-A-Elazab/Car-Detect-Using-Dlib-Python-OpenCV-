# Car-Detect-Using-Dlib-Python-OpenCV-

# Introduction 
 * Dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real world problems. <br>
 * For creating an object detector we use here good way called HOG+SVM that there're very popular and best known for their  performance.
 * It's easy to understand The Histogram of Oriented Gradients [HOG](https://www.learnopencv.com/histogram-of-oriented-gradients/) and Support Vector Machines [SVM](https://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html) but it's difficult to build it from scratch and we use this good api called [dlib](http://dlib.net/)

# Instructions 
 * You need to download image of your object (here is the cars) and put it in the folder.<br>
 * Create your own xml file that contain your paths of cropped object images , you can use imagelab and all details [here](https://github.com/davisking/dlib/tree/master/tools/imglab) <br>
 * Training your object and output "svm" file to use it later in detect and make a test of your training from [here](https://github.com/davisking/dlib/blob/master/python_examples/train_object_detector.py) <br>
 * Finally use the output "svm" file to detect you object (cars here) in the python  file here "detect.py". <br>
 
 # Requirement
   Install Python 2.7 from [here](https://www.python.org/download/releases/2.7/) <br>
   Install OpenCV from [here](http://opencvpython.blogspot.com/2012/05/install-opencv-in-windows-for-python.html) <br>
   Install Numpy from [here](https://pypi.org/project/numpy/) <br>
   Install Dlib for windows from [here](https://pypi.org/project/dlib/) as wheel setup. <br>
   Install Dlib for Linux form [here](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/) <br>
  
# References :- 
 1. http://dlib.net/
 2. https://www.learnopencv.com/histogram-of-oriented-gradients/
 3. https://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html
 4. http://www.coldvision.io/2017/03/23/vehicle-detection-using-opencv-svm-classifier/
 5. https://github.com/danishnazir/Car-Detection-using-HOG-based-Detector-Dlib-
 6. http://www.hackevolve.com/create-your-own-object-detector/
 
 # For Contact :- 
 bassel.alazab@gmail.com
