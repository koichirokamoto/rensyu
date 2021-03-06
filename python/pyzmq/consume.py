import time
import zmq
import random
import util


def consumer(url):
  consumer_id = random.randrange(1, 10005)
  print("I am consumer #%s" % (consumer_id))
  context = zmq.Context()
  # recieve work
  consumer_receiver = context.socket(zmq.PULL)
  consumer_receiver.connect(url)

  try:
    while True:
      work = consumer_receiver.recv_json()
      data = work['num']
      result = {'consumer': consumer_id, 'num': data}
      print(result)
  except KeyboardInterrupt:
    pass


consumer(util.URL)
