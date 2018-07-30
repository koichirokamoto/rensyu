import time

import sample
import util

p = sample.Producer(util.URL)


def main():
  num = 0
  try:
    while True:
      work_message = {'num': num}
      num += 1
      p.send_json(work_message)
      time.sleep(1)
  except KeyboardInterrupt:
    pass


main()
