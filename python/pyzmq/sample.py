import zmq


class Producer:

  def __init__(self, url):
    ctx = zmq.Context()
    self.socket = ctx.socket(zmq.PUSH)
    self.socket.bind(url)

  def send_json(self, obj):
    self.socket.send_json(obj)


class Consumer:

  def __init__(self, url):
    ctx = zmq.Context()
    self.socket = ctx.socket(zmq.PULL)
    self.socket.connect(url)

  def recv_json(self):
    while True:
      data = self.socket.recv_json()
      yield data
