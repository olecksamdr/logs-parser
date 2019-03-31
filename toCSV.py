import os
import time
import argparse

from watchdog.observers import Observer

from parser import parse_file
from modification_handler import ModificationHandler

parser = argparse.ArgumentParser()
parser.add_argument('src_path', help="path to the log file")
args = parser.parse_args()


if __name__ == '__main__':
  parse_file(args.src_path)

  observer = Observer()
  observer.schedule(
    ModificationHandler(args.src_path, parse_file),
    os.path.dirname(args.src_path),
    recursive=False
  )
  observer.start()

  try:
      while True:
          time.sleep(5)
  except KeyboardInterrupt:
      observer.stop()
