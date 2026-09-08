import os
import sys

print("=== Starting Setup for Sanaei Panel ===")

current_dir = os.getcwd()
x_ui_dir = os.path.join(current_dir, "x-ui")

# ۱. دانلود نسخه x-ui در پوشه جاری
if not os.path.exists(x_ui_dir):
    print("Downloading x-ui binary...")
    os.system("curl -sL https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz -o x-ui.tar.gz")
    os.system("tar -zxvf x-ui.tar.gz")
    os.system("rm -f x-ui.tar.gz")

# ۲. اعطای دسترسی‌های لازم
os.system(f"chmod +x {x_ui_dir}/x-ui {x_ui_dir}/bin/xray-linux-* 2>/dev/null")

# ۳. حل مشکل SSL Root CA برای جلوگیری از ارورهای تایید گواهی
os.system("mkdir -p /etc/ssl/certs /etc/pki/tls/certs /usr/share/ca-certificates")
os.system("wget --no-check-certificate https://curl.se/ca/cacert.pem -O /etc/ssl/certs/ca-certificates.crt")
os.system("cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt 2>/dev/null || true")
os.system("cp /etc/ssl/certs/ca-certificates.crt /etc/ssl/cert.pem 2>/dev/null || true")

# ۴. رفتن به پوشه و اجرای پنل
print("=== Launching 3x-ui Core ===")
os.chdir(x_ui_dir)
os.system("./x-ui &")
print("Setup and execution command finished successfully!")
