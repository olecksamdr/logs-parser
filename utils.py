import os
from constants import PROGRAM_DATA_PATH

def get_last_position():
  if os.path.exists(PROGRAM_DATA_PATH):
    with open(PROGRAM_DATA_PATH, 'r') as file:
      return int(file.readline())

  return 0


def set_last_position(position):
  with open(PROGRAM_DATA_PATH, 'w') as file:
    file.write(str(position))

