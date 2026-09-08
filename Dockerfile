FROM python:3.10-slim

WORKDIR /app

# نصب ابزارهای مورد نیاز
RUN apt-get update && apt-get install -y curl wget tar && rm -rf /var/lib/apt/lists/*

# کپی کردن فایل‌های اسکریپت
COPY . /app/

# اجرای اسکریپت پایتون موقع استارت
CMD ["python", "app.py"]