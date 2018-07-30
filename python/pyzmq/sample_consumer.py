import random

import sample
import util

c = sample.Consumer(util.URL)


def main():
  consumer_id = random.randrange(1, 10005)
  print("I am consumer #%s" % (consumer_id))

  try:
    while True:
      work = next(c.recv_json())
      data = work['num']
      result = {'consumer': consumer_id, 'num': data}
      print(result)
  except KeyboardInterrupt:
    pass


main()
