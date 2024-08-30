# CustomPose-Classification-Mediapipe-Badminton Pose
Creating a Custom pose classification using Mediapipe with help of OpenCV

<p align="center">
  <img src='Screenshot 2024-08-30 103424.png'/>
</p>


```
git clone https://github.com/naseemap47/CustomPose-Classification-Mediapipe.git
cd CustomPose-Classification-Mediapipe
```
### Install Dependency
```
pip3 install -r requirements.txt
```

###1.Download Dataset:
**Badminton Poses Dataset:**
```

**Dataset Structure:**
```
Dataset Structure:
```
├── Dataset
│   ├── Footwork
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   ├── ...
│   ├── Backhand
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   ├── ...
.   .
.   .
```
### 2.Create Landmark Dataset for each Classes
```
python3 poseLandmark_csv.py -i <path_to_data_dir> -o <path_to_save_csv>
```
Example:
```
python3 poseLandmark_csv.py -i data/ -o data.csv
```
CSV file will be saved in **<path_to_save_csv>**
### 3.Create DeepLearinng Model to predict Badminton Pose 
```

**To Exit Window - Press Q-key**

### link convert TFLITE 
https://colab.research.google.com/drive/1gelTfXdKFB4d73wUV6HhskgvtluV9xDD?usp=sharing
```
```
**To Exit Window - Press Q-key**
