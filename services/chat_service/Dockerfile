FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src
COPY ./data /app/src/data

EXPOSE 5012

CMD ["python", "src/app.py"]
