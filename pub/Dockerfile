FROM python:3.9
RUN pip install zmq
WORKDIR /app
COPY zmc_publisher.py .
CMD ["python", "zmc_publisher.py"]
