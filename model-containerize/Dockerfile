# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /root

# Copy requirements and install dependencies
COPY requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

# Copy the rest of the application
COPY . /root/.


# Start the app
CMD ["python", "predict.py"]
