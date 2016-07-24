#!/usr/bin/env python
from multiprocessing import Process

import zmq


context = zmq.Context()
channel = context.socket(zmq.PUSH)
channel.connect("tcp://127.0.0.1:5557")


name = raw_input("provide name: ")


def send_message(name):
    while True:
        msg = raw_input("> ")
        channel.send_string("%s: %s" % (name, msg))


def recv_message():
    context = zmq.Context()
    receiver = context.socket(zmq.SUB)
    receiver.connect("tcp://127.0.0.1:5558")
    receiver.setsockopt(zmq.SUBSCRIBE, "")
    while True:
        print receiver.recv_string()


Process(target=recv_message).start()
send_message(name)
