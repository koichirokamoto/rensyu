import time
import zmq
import util


def producer(url):
  context = zmq.Context()
  zmq_socket = context.socket(zmq.PUSH)
  zmq_socket.bind(url)
  # Start your result manager and workers before you start your producers
  num = 0
  try:
    while True:
      work_message = {'num': num}
      num += 1
      zmq_socket.send_json(work_message)
      time.sleep(1)
  except KeyboardInterrupt:
    pass


producer(util.URL)
