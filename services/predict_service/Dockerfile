FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src
COPY ./dataset /app/src/dataset

EXPOSE 5011

CMD ["python", "src/app.py"]
