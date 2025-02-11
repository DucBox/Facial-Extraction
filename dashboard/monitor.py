import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="📊 AI System Dashboard", layout="wide")
st.sidebar.subheader("Ray Dashboard")
st.sidebar.markdown("[🖥️ Mở Ray Dashboard](http://127.0.0.1:9090)")

st.title("📊 AI System Dashboard")

# Đọc số ảnh đã inference từ logs
def count_inference_logs():
    log_file = "../logs/inference.log"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            return sum(1 for _ in f)
    return 0

# Đọc system logs
def load_logs():
    log_file = "../logs/system.log"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            return f.readlines()
    return ["No logs yet."]

# Hiển thị số ảnh đã inference
st.subheader("📸 Inference Statistics")
st.metric("Total Images Processed", count_inference_logs())

# Hiển thị logs hệ thống
st.subheader("📜 System Logs")
logs = load_logs()
st.text_area("Logs", value="".join(logs), height=300)

# Biểu đồ inference theo thời gian
st.subheader("📈 Inference Trend")
log_file = "../logs/inference.log"
if os.path.exists(log_file):
    data = []
    with open(log_file, "r") as f:
        for line in f.readlines():
            if "✅ Đã xử lý" in line:
                data.append(1)
    if data:
        df = pd.DataFrame({"Inference Count": data})
        st.line_chart(df)

# Thêm auto-refresh mỗi 5 giây
st.button("🔄 Refresh")
