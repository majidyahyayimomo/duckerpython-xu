import os
import sys

def main(context):
    context.log("=== Starting Setup for Sanaei Panel ===")
    
    # استفاده از پوشه موقت /tmp که قطعا دسترسی نوشتن دارد
    tmp_dir = "/tmp"
    x_ui_dir = os.path.join(tmp_dir, "x-ui")
    
    context.log(f"Target directory: {x_ui_dir}")
    
    # ۱. دانلود و اکسترکت در صورت عدم وجود پوشه در /tmp
    if not os.path.exists(x_ui_dir):
        context.log("Downloading x-ui binary...")
        os.system(f"curl -sL https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz -o {tmp_dir}/x-ui.tar.gz")
        os.system(f"tar -zxvf {tmp_dir}/x-ui.tar.gz -C {tmp_dir}")
        os.system(f"rm -f {tmp_dir}/x-ui.tar.gz")
    
    # ۲. اعطای دسترسی‌های لازم
    if os.path.exists(x_ui_dir):
        context.log("x-ui directory found. Setting permissions...")
        os.system(f"chmod +x {x_ui_dir}/x-ui {x_ui_dir}/bin/xray-linux-* 2>/dev/null")
        context.log("Setup completed successfully in /tmp.")
        return context.res.text("Sanaei setup script executed in /tmp.")
    else:
        context.error("Failed to create or find x-ui directory in /tmp.")
        return context.res.text("Error: Directory not found", statusCode=500)
