#!/usr/bin/env python3

import requests
import cv2 as cv
import sys
import json
import argparse
import csv
import os
from typing import Callable, Tuple, Dict
from pathlib import Path

URL = 'http://localhost:9200/test_index/_doc'

def main(dir: str, list_file: str):
  images_map = read_list(list_file)
  for (filename, title) in images_map.items():
    print(f'[+] indexing {filename}')
    file_path = f'{dir}/{filename}'
    if Path(file_path).is_file():
      index_image(file_path, title)
    else:
      print(' [-] not found')

def read_list(list_file: str) -> Dict[str, str]:
  m = {}
  with open(list_file) as fh:
    csv_reader = csv.reader(fh)
    for row in csv_reader:
      m[f'{row[1]}.jpg'] = row[0]
  return m

def index_image(img_file: str, title: str):
  # print(f'[+] indexing file {img_file}')
  img = cv.imread(img_file)
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  # extractor = cv.SIFT_create(50);
  extractor = cv.ORB_create(50)
  kp, desc = extractor.detectAndCompute(img, None)
  # print(f'[+] detected {len(kp)} keypoints')
  desc_mat = desc.tolist()
  for i, row in enumerate(desc_mat):
    print(f'\r  [+] indexing vector {i+1}/{len(desc_mat)}', end='', flush=True)
    submit_vector(row, title)
  print()
  print(' [+] done')

def submit_vector(vector: list, title: str):
  res = requests.post(URL, json={'image_vec': vector, 'title': title})
  res.raise_for_status()

def readdir(dir: str, file_filter: Callable[[str], bool] = lambda f : True) -> Tuple[str, str]:
  for f in os.listdir(dir):
    if file_filter(f):
        yield (f, os.path.join(dir, f))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--dir', required=True, type=str)
  parser.add_argument('--list_file', required=True, type=str)
  args = parser.parse_args()
  main(args.dir, args.list_file)
