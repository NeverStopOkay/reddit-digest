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

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Expose Airflow UI
EXPOSE 8080

# Use custom entrypoint
ENTRYPOINT ["./entrypoint.sh"]