import csv
from datetime import datetime

from utils import get_last_position, set_last_position

def parse_line(line):
  row = line.strip('{} \r\n').split('" "')

  # line could be partialy written to the logs, so we need to check it
  if len(row) == 30:
      row = list(map(lambda str: str.strip('"'), row))

      date = datetime.fromtimestamp(int(row[3]))
      row[3] = date.strftime('%d-%m-%Y')
      row.insert(4, date.strftime('%H:%M'))

      return row

  return None


def parse_file(path):
  with open(path, 'r', encoding='iso-8859-1') as srcFile, \
      open('dest.csv', 'a') as dstFile:
    writer = csv.writer(dstFile)
    # writer.writerow(HEADERS)

    srcFile.seek(get_last_position())

    line = srcFile.readline()
    while line:
      result = parse_line(line)

      if result is not None:
        writer.writerow(parse_line(line))
        set_last_position(srcFile.tell())

      line = srcFile.readline()

