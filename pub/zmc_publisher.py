import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")  # Bind to port

while True:
	socket.send_string("r 90")  # Sending 'r' direction with 90° angle
	print("Sent: r 90")
	time.sleep(1)
	socket.send_string("l 90")  # Sending 'l' direction with 90° angle
	print("Sent: l 90")
	time.sleep(1)

	socket.send_string("r 0")  # Sending 'r' direction with 90° angle
	print("Sent: r 0")
	time.sleep(1)
	socket.send_string("l 9")  # Sending 'l' direction with 90° angle
	print("Sent: l 0")
	time.sleep(1)