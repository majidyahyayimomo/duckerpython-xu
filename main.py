import os
import subprocess

def main(context):
    context.log("=== Testing Network & Download ===")
    
    tmp_dir = "/tmp"
    url = "https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz"
    
    # استفاده از subprocess برای گرفتن ارور دقیقِ curl
    result = subprocess.run(["curl", "-sL", url, "-o", f"{tmp_dir}/test.tar.gz"], capture_output=True, text=True)
    
    context.log(f"Curl return code: {result.returncode}")
    context.log(f"Curl stderr: {result.stderr}")
    
    files = os.listdir(tmp_dir)
    context.log(f"Files in /tmp now: {files}")
    
    return context.res.text(f"Curl Code: {result.returncode}, Files: {files}")
