# ML_Object_Detection
- This tool assists you in training your object detection model and converting it to a TFLite model, which can be easily deployed on your device.
- The training framework utilizes [TensorFlow Object Detection API](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/) on TensorFlow 2 and TensorFlow 1.
- The notebooks simplify the complicated installation steps and provide an easy-to-use approach for data preparation, training, and conversion.
## 1. First step
#### 1. Install virtual env  
- If you haven't installed [NuEdgeWise](https://github.com/OpenNuvoton/NuEdgeWise), please follow these steps to install Python virtual environment and ***choose `NuEdgeWise_env`***.
- Skip if you have done.
#### 2. Install the Visual C++ 2015 build tools
- Log in to https://my.visualstudio.com/Downloads (You will need a free Microsoft account).
- Enter 'Build Tools' in the search bar.
- Select 'Visual Studio 2015 Update 3' on the left side.
- Click on 'DVD' under 'Visual C++ Build Tools...' and initiate the download.
- Follow the installation steps to complete the installation process.
<img src="https://user-images.githubusercontent.com/105192502/209085872-18dadffb-aa0d-4c07-9780-f2a1237b2211.png" width="60%">

#### 3. Install [git windows version](https://gitforwindows.org/)
- Git is required during the 5th step. 
#### 4. Download this git folder 
- `git clone https://github.com/OpenNuvoton/ML_tf2_object_detection_nu.git`
- Or you can download the zip file directly
#### 5. Object Detection API installation
- Open Anaconda with administrator privileges and select the `NuEdgeWise_env`. Utilize `setup_objdet_tf2.ipynb` to install the remaining packages.
#### 6. TF1 Object Detection API installation (Optional)
- If you wish to use ssd_mobileNetv3, TensorFlow 1 is required, so you need to create a new Python virtual environment not using `NuEdgeWise_env`.
- First, refer to `create_conda_env_tf1.ipynb`, and then proceed to `setup_objdet_tf1.ipynb`.
---
## 2. Work Flow
<img src="https://user-images.githubusercontent.com/105192502/203241236-e6c729f4-8087-439c-9b0d-0fffbf602c71.png" width="80%">

### 1. data prepare

- Open `create_data.ipynb` located in `image_dataset`. Ensure that you execute it in a TensorFlow 2 environment. 
- This process will handle the downloading of open-source images or labeling your customized images to create a training dataset.
- The tutorial for this process is provided within the `create_data.ipynb` notebook.

### 2. train & tflite model creating

- Open the workspace folder.
- Users need to choose either the TensorFlow 1 or TensorFlow 2 environment based on their training model.
- This process will handle training, mAP evaluation, and TFLite conversion.
- The tutorial for this process is provided within the notebook.

#### tensorflow2
- Use `train_evl_monitor_tf2.ipynb` for an easy-to-use user interface that facilitates training, evaluation, and monitoring.
- Use `convert_tflite_tf2.ipynb` for an easy-to-use user interface that aids in converting to TFLite format.

[alternative way]:
- Open `train_cmd_tf2.ipynb`.
- Google's object detection support models: [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) 

#### tensorflow1
- Open `train_cmd_tf1.ipynb`. This should be excuted in tf1 env (Check `create_conda_env_tf1.ipynb` & `setup_objdet_tf1.ipynb` to create tf1 env).
- Google's object detection support models: [TensorFlow 1 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md) 

### 3. evaluation & test

- Open `test_tflite.ipynb` located in the `workspace` folder. Make sure to execute it in a TensorFlow 2 environment.
- Evaluate the results of the TFLite model using your own dataset.
- The tutorial for this process is provided within the `test_tflite.ipynb` notebook.

## 3. Inference code
- The MPU example code: [MA35D1_machine_learning](https://github.com/OpenNuvoton/MA35D1_Linux_Applications/tree/master/machine_learning)
