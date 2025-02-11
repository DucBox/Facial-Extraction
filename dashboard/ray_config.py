import ray

ray.init(ignore_reinit_error=True, dashboard_host="0.0.0.0", dashboard_port=8265)

print(f"📊 Ray Dashboard chạy tại: http://127.0.0.1:8265")
