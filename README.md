# CustomPose-Classification-Mediapipe: Badminton Pose Classification

This project aims to create a custom pose classification model for badminton using MediaPipe and OpenCV.

<p align="center">
  <img src='Screenshot 2024-08-30 103424.png'/>
</p>

## Getting Started

### 1. Clone the Repository and Install Dependencies

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/naseemap47/CustomPose-Classification-Mediapipe.git
cd CustomPose-Classification-Mediapipe
pip3 install -r requirements.txt
```

### 2. Download the Dataset

Download the badminton pose dataset and organize it in the following structure:

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

### 3. Create a Landmark Dataset for Each Class

Run the following script to create a landmark dataset from the pose images:

```bash
python3 poseLandmark_csv.py -i <path_to_data_dir> -o <path_to_save_csv>
```

**Example:**

```bash
python3 poseLandmark_csv.py -i data/ -o data.csv
```

The CSV file will be saved at the specified location.

### 4. Convert CSV to TFLite Model

After obtaining the CSV file, convert it to a TFLite model using [this Google Colab link](https://colab.research.google.com/drive/1gelTfXdKFB4d73wUV6HhskgvtluV9xDD?usp=sharing).

### 5. Run the Interface Program

Once you have the TFLite model, run the interface program.

**To Exit Window - Press Q-key**
