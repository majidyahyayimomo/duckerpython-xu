import os
import urllib.request

def main(context):
    context.log("=== Setting up 3x-ui in /tmp ===")
    
    tmp_dir = "/tmp"
    url = "https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz"
    file_path = os.path.join(tmp_dir, "x-ui.tar.gz")
    x_ui_dir = os.path.join(tmp_dir, "x-ui")
    
    # دانلود و استخراج در صورت عدم وجود
    if not os.path.exists(x_ui_dir):
        urllib.request.urlretrieve(url, file_path)
        os.system(f"tar -zxvf {file_path} -C {tmp_dir}")
        os.system(f"rm -f {file_path}")
    
    # اعطای دسترسی اجرایی
    os.system(f"chmod +x {x_ui_dir}/x-ui {x_ui_dir}/bin/xray-linux-* 2>/dev/null")
    
    # بررسی وجود فایل اجرایی
    is_executable = os.access(f"{x_ui_dir}/x-ui", os.X_OK)
    context.log(f"Is x-ui executable? {is_executable}")
    
    return context.res.text(f"Setup complete! x-ui is executable: {is_executable}")
