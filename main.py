import os
import subprocess
import urllib.request
import glob

def main(context):
    context.log("=== Smart Setup and Execution for x-ui ===")
    
    tmp_dir = "/tmp"
    url = "https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz"
    file_path = os.path.join(tmp_dir, "x-ui.tar.gz")
    
    try:
        # دانلود در صورت عدم وجود
        if not os.path.exists(file_path):
            context.log("Downloading x-ui...")
            urllib.request.urlretrieve(url, file_path)
            
        # استخراج فایل
        context.log("Extracting tarball...")
        os.system(f"tar -zxvf {file_path} -C {tmp_dir}")
        
        # پیدا کردن هوشمند مسیر باینری x-ui در /tmp
        x_ui_path = None
        for root, dirs, files in os.walk(tmp_dir):
            if "x-ui" in files:
                candidate = os.path.join(root, "x-ui")
                if os.path.isfile(candidate) and not candidate.endswith(".tar.gz"):
                    x_ui_path = candidate
                    break
                    
        if x_ui_path and os.path.exists(x_ui_path):
            os.system(f"chmod +x {x_ui_path}")
            context.log(f"Found binary at: {x_ui_path}")
            
            # اجرای تست ورژن
            result = subprocess.run([x_ui_path, "-v"], capture_output=True, text=True, timeout=5)
            output = result.stdout or result.stderr
            return context.res.text(f"x-ui executed successfully! Output: {output}")
        else:
            files_in_tmp = os.listdir(tmp_dir)
            return context.res.text(f"Binary not found. Contents: {files_in_tmp}", statusCode=500)
            
    except Exception as e:
        context.error(f"Error: {str(e)}")
        return context.res.text(f"Error: {str(e)}", statusCode=500)
