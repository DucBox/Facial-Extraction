import sys
import os

# Thêm thư mục gốc của project vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.detection import HeadDetector

head_detect = HeadDetector()
img_path = '/Users/ngoquangduc/Desktop/AI_Project/Facial_Extraction/data/test/img_1.jpg'
head_detect.detect_heads(img_path)