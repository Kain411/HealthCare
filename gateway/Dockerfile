FROM python:3.11-slim

WORKDIR /app

# Cài đặt các phụ thuộc từ requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn từ thư mục src vào /app/src
COPY ./src /app/src

# Thiết lập làm việc trong thư mục src (nếu cần)

EXPOSE 8001

# Chạy tệp gateway.py
CMD ["python", "src/gateway.py"]
