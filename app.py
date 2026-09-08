import os
import sys

print("=== Starting Setup for Sanaei Panel ===")

# ۱. دانلود آخرین نسخه x-ui در صورت عدم وجود
if not os.path.exists("/app/x-ui"):
    print("Downloading x-ui binary...")
    os.system("curl -sL https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz -o x-ui.tar.gz")
    os.system("tar -zxvf x-ui.tar.gz")
    os.system("rm -f x-ui.tar.gz")

# ۲. اعطای دسترسی‌های لازم
os.system("chmod +x /app/x-ui/x-ui /app/x-ui/bin/xray-linux-* 2>/dev/null")

# ۳. حل مشکل SSL Root CA برای جلوگیری از ارورهای تایید گواهی
os.system("mkdir -p /etc/ssl/certs /etc/pki/tls/certs /usr/share/ca-certificates")
os.system("wget --no-check-certificate https://curl.se/ca/cacert.pem -O /etc/ssl/certs/ca-certificates.crt")
os.system("cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt 2>/dev/null || true")
os.system("cp /etc/ssl/certs/ca-certificates.crt /etc/ssl/cert.pem 2>/dev/null || true")

# ۴. تغییر مسیر به پوشه x-ui و اجرای مستقیم باینری
print("=== Launching 3x-ui Core ===")
os.chdir("/app/x-ui")
os.execv("./x-ui", ["./x-ui"])