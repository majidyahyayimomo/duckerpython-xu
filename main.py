import os
import subprocess
import urllib.request

def main(context):
    context.log("=== Testing x-ui Binary Execution ===")
    
    tmp_dir = "/tmp"
    x_ui_path = os.path.join(tmp_dir, "x-ui", "x-ui")
    
    # تست گرفتن ورژن یا اجرای آنی باینری
    try:
        result = subprocess.run([x_ui_path, "-v"], capture_output=True, text=True, timeout=5)
        output = result.stdout or result.stderr
        context.log(f"Binary output: {output}")
        return context.res.text(f"x-ui executed successfully! Output: {output}")
    except Exception as e:
        context.error(f"Execution error: {str(e)}")
        return context.res.text(f"Error running binary: {str(e)}", statusCode=500)
