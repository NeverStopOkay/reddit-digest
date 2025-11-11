# Dockerfile (Single-Container for Render)
FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Airflow init & user creation (runs on start)
RUN airflow db init && \
    airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin

# Expose Airflow UI
EXPOSE 8080

# Start scheduler & webserver in background (simple for Render)
CMD airflow scheduler & airflow webserver --port 8080