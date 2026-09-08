import os
import sys

def main(context):
    context.log("=== Starting Setup for Sanaei Panel ===")
    
    current_dir = os.getcwd()
    x_ui_dir = os.path.join(current_dir, "x-ui")
    
    context.log(f"Working directory: {current_dir}")
    
    # ۱. دانلود و اکسترکت در صورت عدم وجود پوشه
    if not os.path.exists(x_ui_dir):
        context.log("Downloading x-ui binary...")
        os.system(f"curl -sL https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz -o {current_dir}/x-ui.tar.gz")
        os.system(f"tar -zxvf {current_dir}/x-ui.tar.gz -C {current_dir}")
        os.system(f"rm -f {current_dir}/x-ui.tar.gz")
    
    # ۲. چک کردن اینکه آیا پوشه بالاخره ساخته شد یا نه
    if os.path.exists(x_ui_dir):
        context.log("x-ui directory exists. Setting permissions...")
        os.system(f"chmod +x {x_ui_dir}/x-ui {x_ui_dir}/bin/xray-linux-* 2>/dev/null")
        context.log("Setup completed successfully.")
        return context.res.text("Sanaei setup script executed.")
    else:
        context.error("Failed to create or find x-ui directory.")
        return context.res.text("Error: Directory not found", status_code=500)
