import os
import urllib.request

def main(context):
    context.log("=== Downloading via Python urllib ===")
    
    tmp_dir = "/tmp"
    url = "https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz"
    file_path = os.path.join(tmp_dir, "x-ui.tar.gz")
    
    try:
        # دانلود فایل با ماژول داخلی پایتون
        urllib.request.urlretrieve(url, file_path)
        context.log("Download completed successfully!")
        
        # استخراج فایل
        os.system(f"tar -zxvf {file_path} -C {tmp_dir}")
        
        files = os.listdir(tmp_dir)
        context.log(f"Files in /tmp: {files}")
        
        return context.res.text(f"Success! Files: {files}")
    except Exception as e:
        context.error(f"Download failed: {str(e)}")
        return context.res.text(f"Error: {str(e)}", statusCode=500)
