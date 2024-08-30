import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

path_saved_model = 'C:/Users/ilham/Desktop/shadowgila/model7.tflite' # load TensorFlow Lite model
image_path = 'C:/Users/ilham/Desktop/shadowgila/dataset1/footwork/footwork (52).jpg'
threshold = 0.8 # confidence

class_names = ['backhand', 'footwork', 'forehand', 'unknownpose']

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Load saved TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path=path_saved_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Read image
img = cv2.imread(image_path)
if img is None:
    print('[ERROR] Image not found')
    exit()

img_resize = cv2.resize(img, (320, 320))
img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
result = pose.process(img_rgb)

# Draw the pose annotation on the image.
img.flags.writeable = True
mp_drawing.draw_landmarks(
    img_resize, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
    mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4), 
    mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
)

if result.pose_landmarks:
    lm_array = np.array([[lm.x, lm.y, lm.z, lm.visibility] for lm in result.pose_landmarks.landmark]).flatten()
    # Reshape for model input
    lm_array = lm_array.reshape(1, lm_array.shape[0])
    interpreter.set_tensor(input_details[0]['index'], lm_array.astype(np.float32))
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])
    if np.max(predictions) > threshold:
        pose_class = class_names[np.argmax(predictions)]
        print('Predictions: ', predictions)
        print('Predicted Pose Class: ', pose_class)
    else:
        pose_class = 'Unknown Pose'
        print('[INFO] Predictions are below the given confidence!')

    # Show Result
    img = cv2.putText(img_resize, f'{pose_class}', (40, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

cv2.imshow('Output Image', img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
