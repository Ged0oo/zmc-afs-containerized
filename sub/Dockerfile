FROM python:3.9

# Install dependencies
RUN pip install pyserial zmq
RUN apt update && apt install -y iputils-ping netcat-openbsd tcpdump

# Set working directory
WORKDIR /app

# Copy script into the container
COPY zmq_serial.py .

# Ensure script is executable
RUN chmod +x /app/zmq_serial.py

# Run script on container start
CMD ["python3", "/app/zmq_serial.py"]
