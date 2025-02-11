import cv2
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input

def preprocess_image(img, size=(224, 224)):
    """
    Chuyển ảnh về định dạng phù hợp cho model ResNet.
    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, size)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img
