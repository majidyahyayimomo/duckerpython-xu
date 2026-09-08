import os
import subprocess
import urllib.request
import time
import socket

def main(context):
    context.log("=== Starting 3x-ui Panel Inside Serverless ===")
    
    tmp_dir = "/tmp"
    url = "https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz"
    file_path = os.path.join(tmp_dir, "x-ui.tar.gz")
    
    # ۱. دانلود و استخراج (اگر قبلاً انجام نشده باشه)
    if not os.path.exists(file_path):
        urllib.request.urlretrieve(url, file_path)
        os.system(f"tar -zxvf {file_path} -C {tmp_dir}")
        os.system(f"rm -f {file_path}")
        
    # ۲. پیدا کردن مسیر باینری
    x_ui_path = None
    for root, dirs, files in os.walk(tmp_dir):
        if "x-ui" in files:
            candidate = os.path.join(root, "x-ui")
            if os.path.isfile(candidate) and not candidate.endswith(".tar.gz"):
                x_ui_path = candidate
                break
                
    if not x_ui_path:
        return context.res.text("Error: x-ui binary not found", statusCode=500)
        
    os.system(f"chmod +x {x_ui_path}")
    
    # ۳. اجرای پنل در پس‌زمینه داخل کانتینر
    context.log("Launching x-ui process...")
    process = subprocess.Popen([x_ui_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # ۴. کمی صبر می‌کنیم تا وب‌سرور داخلی بالا بیاید
    time.sleep(3)
    
    # ۵. بررسی اینکه آیا پورت پیش‌فرض (مثلاً 2053) روی لوکال‌هاست پاسخ می‌دهد یا خیر
    # پورت پیش‌فرض 3x-ui معمولاً 2053 است
    port = 2053
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    
    is_port_open = (result == 0)
    context.log(f"Is local port {port} open? {is_port_open}")
    
    return context.res.text(f"Panel execution triggered! Local port {port} open status: {is_port_open}")
