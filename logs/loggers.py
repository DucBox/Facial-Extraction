import logging
import os

# Đảm bảo thư mục logs tồn tại
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Lấy thư mục logs/
LOG_DIR = os.path.join(BASE_DIR)  # logs/ nằm ngay trong Facial_Extraction/
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name, log_file, level=logging.INFO):
    log_path = os.path.join(LOG_DIR, log_file)
    logger = logging.getLogger(name)

    # Kiểm tra nếu logger chưa có handler, tránh bị trùng log
    if not logger.hasHandlers():
        handler = logging.FileHandler(log_path, mode='a')
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(level)
    return logger

# Đảm bảo đường dẫn file log đúng
print(f"✅ Logger Paths: \n - System: {os.path.join(LOG_DIR, 'system.log')} \n - Inference: {os.path.join(LOG_DIR, 'inference.log')} \n - Training: {os.path.join(LOG_DIR, 'training.log')}")

# Tạo 3 loại logger
training_logger = setup_logger("training", "training.log")
inference_logger = setup_logger("inference", "inference.log")
system_logger = setup_logger("system", "system.log")

# Hàm tiện ích ghi log
def log_training(message):
    training_logger.info(f"[Training] {message}")
    for handler in training_logger.handlers:
        handler.flush()

def log_inference(message):
    inference_logger.info(f"[Inference] {message}")
    for handler in inference_logger.handlers:
        handler.flush()

def log_system(message):
    system_logger.info(f"[System] {message}")
    for handler in system_logger.handlers:
        handler.flush()
