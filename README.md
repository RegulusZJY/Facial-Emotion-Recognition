# Facial Emotion Recognition
## Python
  Description:  
  Our faces have complex emotions. Our program can recognize our facial emotions and give the probability of having these emotions.  

  Environment:  
  Python version: 3.8.8  
  keras: 2.4.3  
  matplotlib: 3.3.4  
  numpy: 1.19.5  
  opencv: 4.0.1  
  pandas: 1.2.4  
  tensorflow: 2.3.0  
  Jupyter: 1.0.0  
  Jupyterlab: 3.0.14  

  Folders and files:
  The src folder contains an ipynb file for training data sets, an ipynb file for calling the camera to obtain video, the "data" folder (which contains three data sets), and the "model" folder (which contains two trained models and a CNN network Python file).  
  Output folder contains Accuracy_Loss and Emotion_Recog folder. Accuracy_Loss has the accuracy and loss graphs, and trained history information.  
  Emotion_Recog has the sreenshots that use the camera to test our emotions, some emotions are found in Google pictures, the result is good.  
  In addition, here is a video that Zhang Junyan recorded while testing the program.  

  Run:  
  Open emotion_recognition_camera.ipynb (in src folder) by Jupyter notebook. You can run Jupyter with Anaconda or VSCode. Both compilers can download and install Jupyter.   

  Usage:  
  The program will create a window to display the scene captured by the webcam and a window to represent the probability of emotion detected, as well as the emotion in front of the camera. Input is the picture obtained through the camera, or you can modify the camera information in the ipynb file and fill in a path containing the video to be detected  

  Tips:  
  We have provided two well-trained models in the model file. Both of them have high accuracy and can better recognize emotions. You can also run a training file to retrain a model.  

  Source of data set:  
  https://www.kaggle.com/datasets/msambare/fer2013  
  https://www.kaggle.com/datasets/debanga/facial-expression-recognition-challenges  

  Test pictures from:  
  https://www.google.com.hk/search?q=sad+emotion&newwindow=1&sxsrf=ALiCzsYS-Y4uAfx6HD-sfcOjunmp713Bow:1653750375154&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj50aGdvIL4AhUaSTABHaZrDLUQ_AUoAXoECAEQAw&biw=1536&bih=722&dpr=1.25  

  https://www.google.com.hk/search?q=disgust+emotion&tbm=isch&ved=2ahUKEwiRhPKdvIL4AhUWsXIEHRHKCygQ2-cCegQIABAA&oq=disgust+emotion&gs_lcp=CgNpbWcQAzIECCMQJzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzoFCAAQgAQ6BAgAEB5Q4wpYnhVgxB9oAHAAeACAAa4CiAH3FJIBBTItNS40mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=aDqSYpGwHJbiytMPkZSvwAI&bih=722&biw=1536  

  https://www.google.com.hk/search?q=fear+emotion&tbm=isch&ved=2ahUKEwja1MWlvIL4AhXarnIEHVrpC8sQ2-cCegQIABAA&oq=fear+emotion&gs_lcp=CgNpbWcQAzIECCMQJzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQE1DUA1ioB2CUCWgAcAB4AIABsgKIAa4JkgEFMi0yLjKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=eDqSYtq4H9rdytMP2tKv2Aw&bih=722&biw=1536  

  https://www.google.com.hk/search?q=angry+emotion&tbm=isch&ved=2ahUKEwjU8aWqvIL4AhWXrXIEHfwBDmkQ2-cCegQIABAA&oq=angry+emotion&gs_lcp=CgNpbWcQAzIECCMQJzIGCAAQHhAHMgYIABAeEAcyBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB46BAgAEBM6BggAEB4QDDoGCAAQHhAIUNAGWMMVYIgZaABwAHgAgAG4AogB2RKSAQUyLTQuNJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=gjqSYtSoHZfbytMP_IO4yAY&bih=722&biw=1536  

  https://www.google.com.hk/search?q=surprised+emotion&tbm=isch&ved=2ahUKEwil_PKuvIL4AhWjVDUKHeDPAoIQ2-cCegQIABAA&oq=surprised+emotion&gs_lcp=CgNpbWcQAzIGCAAQHhAHMgYIABAeEAcyBggAEB4QBzIGCAAQHhAHMgYIABAeEAcyBggAEB4QBzIGCAAQHhAHMgYIABAeEAcyBggAEB4QBzIGCAAQHhAHOgQIIxAnOgQIABAeULsIWPMUYLgWaABwAHgAgAG3AogBmRWSAQUyLTMuNpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=jDqSYqWGCKOp1QHgn4uQCA&bih=722&biw=1536  
