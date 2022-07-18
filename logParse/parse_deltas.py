#!/usr/bin/env python3

import csv
import datetime
import sys
import time

start_file = str(sys.argv[1])
end_file = str(sys.argv[2])
deltas_file = str(sys.argv[3])

def read_csv(filepath):
  with open(filepath, "r") as csvfile:
    read_file = csv.reader(csvfile)
    d = {}
    for r in read_file:
      d[r[0]] = {"timestamp": r[1], "ip": r[2]}
    return d

def convert_date(s):
  e = time.mktime(datetime.datetime.strptime(s, "%m/%d/%Y %H:%M:%S").timetuple())
  return e

def get_deltas(t1, t2):
  d = convert_date(t2) - convert_date(t1)
  return d 

if __name__ == "__main__":
  starts = read_csv(start_file)
  ends = read_csv(end_file)
  list = []
  for id in starts:
    start_time = starts[id]["timestamp"]
    end_time = ends[id]["timestamp"]
    ip = starts[id]["ip"]
    delta = get_deltas(start_time, end_time)
    list.append(f"{ip},{delta}\n")

  with open(deltas_file, "w") as csvout:
    writer = csv.writer
    csvout.writelines(list)
    