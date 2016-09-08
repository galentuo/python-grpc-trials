"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import helloworld_pb2


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.Request(name='world'))
  print("Greeter client received: " + response.message)


if __name__ == '__main__':
  run()
