"""Python 3.6"""

import asyncio
from concurrent.futures import ThreadPoolExecutor
import functools
import logging
import random
import time
import traceback

# Initialize seed.
random.seed(4096)

# Set logging for debug.
logging.basicConfig(level=logging.DEBUG)

queue = asyncio.Queue()


def set_to_queue(n):
  print(n)
  queue.put_nowait({'content': 'This is No.{}'.format(n), 'wait': n})


def print_data(content):
  print(content)


async def main():
  while True:
    loop = asyncio.get_event_loop()
    data = await queue.get()
    loop.call_later(data['wait'], functools.partial(
        print_data, data['content']))


def run():
  print('run')
  for i in range(0, 10):
    n = random.randint(0, 10)
    set_to_queue(n)


if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  executor = ThreadPoolExecutor(max_workers=1)
  executor.submit(run)

  loop.run_until_complete(main())
  loop.close()

  print('finish')
