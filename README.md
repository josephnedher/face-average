# face-average
A simple python script to combine pictures of several persons  to make a new image 

# INITIALIZATION AND REQUIREMENTS

 ## UBUNTU
  
     $ sudo apt-get install build-essential cmake
     $ sudo apt-get install libgtk-3-dev
     $ sudo apt-get install libboost-all-dev
     $ wget https://bootstrap.pypa.io/get-pip.py
     $ sudo python get-pip.py
     $ pip install numpy
     $ pip install scipy
     $ pip install scikit-image
     $ pip install opencv-python
     $ pip install dlib
  Installation of dlib may take some time  so have a coffee
  I personally recommend you to try the all installation on a virtual enviornment
  For detailed installation process you can visit here https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/
  
  ## HOW TO FIRE THE SCRIPT
    
   In the folder there are three files
   
  * fetch.py
  
     I really write this script for fetching my college students image to the folder images.
     
         $ python fetch.py username1 username2  .......
     
     I used sys.argv for this you can type as many username as you wanted generally the admission number.If anyone who doesnt      belong  to our college or you want other images to combine then just go to next step
     
  * facedetect.py 
    
    This script mainly used to detect face landmarks and it take three arguments
         you have to download the dataset provided by opencv and extract it in the this folder 
         
                http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
    
                $ python facedetect.py  shape_predictor_68_face_landmarks.dat  images
          
     shape predictor is dataset of images in .dat format
     
     images is the important folder to add the images in specific format 
     
     ** note please before you execute this script please add the images in images folder and execute the script
     
  * mix.py
      
        $ python mix.py 
    This script will combine the images into a new image and popup the image in the screen
    
    
 ## EXECUTION AT A GLANCE 
     
     $ git clone https://github.com/josephnedher/face-average.git
     $ cd face-average 
       extract your .dat file here
     $ mkdir images   
       add your images in the images folder
     $ python facedetect.py  shape_predictor_68_face_landmarks.dat  images
        
        
