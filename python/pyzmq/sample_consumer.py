import random

from absl import app as abls_app
from absl import flags
import sample
import util


def define_flags():
  """Add flags for running sample consumer."""
  flags.DEFINE_integer(name='start', default=1,
                       help='start of consumer id range')
  flags.DEFINE_integer(name='end', default=10005,
                       help='end of consumer id range')


def main(_):
  c = sample.Consumer(util.URL)
  consumer_id = random.randrange(1, 10005)
  print('I am consumer #%s' % (consumer_id))

  try:
    while True:
      work = next(c.recv_json())
      data = work['num']
      result = {'consumer': consumer_id, 'num': data}
      print(result)
  except KeyboardInterrupt:
    pass


if __name__ == '__main__':
  define_flags()
  abls_app.run(main)
