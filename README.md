# ML_tf2_object_detection_nu
- This Tool help you train your object-detection model and convert to tflite-model which is easy to deploy on your device.
- The training framework is using Tensorflow object detection API on Tensoflow-2 & Tensorflow-1.
- The notebooks help you simplify the complicated installation steps and easy to use data preparing, training and converting. 
## First step
- Download the [anaconda](https://www.anaconda.com/products/distribution) and install it. (If you are familiar with python env creating, you can skip this step)
- `git clone --recurse-submodules https://github.com/OpenNuvoton/ML_tf2_object_detection_nu.git`
- Use `setup_objdet_tf2_env.ipynb` in `ML_tf2_object_detection_nu/` to create the object-detection python running environment.
---
## Work Flow
<img src="https://user-images.githubusercontent.com/105192502/203241236-e6c729f4-8087-439c-9b0d-0fffbf602c71.png" width="80%">

## data prepare
- Open `create_data.ipynb` in `image_dataset`. This should be excuted in tf2 env (Check `setup_objdet_tf2_env.ipynb` to create tf2 env).
- This process will handle downloading open source images or labeling your customized images to create train dataset.
- The tutorial is in this notebook.

## train & model creating
- User need to choose tf1 or tf2 environment basing on user's training model.
- This process will handle training, mAP evaluation and converting tflite.
- The tutorial is in the notebook.
### tensorflow2
- Open `train_cmd_tf2.ipynb` in `workspace`. This should be excuted in tf2 env.
- Google's object detection support models: [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) 
### tensorflow1
- Open `train_cmd_tf1.ipynb` in `workspace`. This should be excuted in tf1 env (Check `setup_objdet_tf1_env.ipynb` to create tf1 env).
- Google's object detection support models: [TensorFlow 1 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md) 

## evaluation & test
- Open `test_tflite.ipynb` in `workspace`. This should be excuted in tf2 env.
- Examine/evaluation the result of tflite model with user's dataset. 
- The tutorial is in this notebook.
