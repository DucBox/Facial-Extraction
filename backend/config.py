import os

# Đường dẫn đến model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_YOLO_PATH = os.path.join(BASE_DIR, "../models/head_detect.pt")
MODEL_RESNET_PATH = os.path.join(BASE_DIR, "../models/facial_extract.h5")

# Danh sách nhãn của ResNet
LABELS = ['beard', 'earrings', 'female', 'glass', 'hat', 'male']
