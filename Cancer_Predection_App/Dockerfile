# Use a lightweight Python image
FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

COPY requirements.txt requirements.txt
# Install dependencies

RUN pip3 install -r requirements.txt

COPY . .

# Start the Flask application on the required port
CMD ["python3", "app.py"]
