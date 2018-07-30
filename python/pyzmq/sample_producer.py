import time

from absl import app as absl_app
from absl import flags
import sample
import util

p = sample.Producer(util.URL)


def define_flags():
  """Add flags for running sample producer."""
  flags.DEFINE_integer(name='sleep', default=1, help='sleep time')


def main(_):
  num = 0
  try:
    while True:
      work_message = {'num': num}
      num += 1
      p.send_json(work_message)
      time.sleep(FLAGS.sleep)
  except KeyboardInterrupt:
    pass


if __name__ == '__main__':
  define_flags()
  FLAGS = flags.FLAGS
  absl_app.run(main)
