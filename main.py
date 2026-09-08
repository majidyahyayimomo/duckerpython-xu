import os

def main(context):
    context.log("=== Debugging Directory Contents ===")
    
    tmp_dir = "/tmp"
    
    # دانلود و اکسترکت فایل
    os.system(f"curl -sL https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz -o {tmp_dir}/x-ui.tar.gz")
    os.system(f"tar -zxvf {tmp_dir}/x-ui.tar.gz -C {tmp_dir}")
    os.system(f"rm -f {tmp_dir}/x-ui.tar.gz")
    
    # لیست کردن تمام فایل‌ها و پوشه‌های داخل /tmp
    files = os.listdir(tmp_dir)
    context.log(f"Files in /tmp: {files}")
    
    return context.res.text(f"Contents: {str(files)}")
