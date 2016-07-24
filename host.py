#!/usr/bin/env python
import zmq


context = zmq.Context()

channel = context.socket(zmq.PULL)
channel.bind("tcp://127.0.0.1:5557")

publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:5558")

while True:
    msg = channel.recv_string()
    print msg
    publisher.send_string(msg)
