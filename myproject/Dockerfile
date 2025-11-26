# Step 1: استخدام صورة Python الرسمية
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# نسخ ملفات المشروع
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port
EXPOSE 8000

# أمر تشغيل السيرفر
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
