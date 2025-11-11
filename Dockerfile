# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system deps for Airflow
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose Airflow webserver
EXPOSE 8080

CMD ["airflow", "webserver"]