FROM python:3.9
RUN pip install pyserial zmq
WORKDIR /app
COPY zmq_serial.py .
CMD ["python", "zmq_serial.py"]
