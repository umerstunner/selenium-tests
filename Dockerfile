FROM python:3.9-slim
# Install dependencies for Selenium and headless Chrome
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    curl \
    && rm -rf /var/lib/apt/lists/*
# Set up Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
# Set working directory
WORKDIR /app
# Copy Selenium test scripts into the container
COPY . /app
# Run the Selenium tests
CMD ["python", "selenium_tests.py"]
