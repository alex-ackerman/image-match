#!/usr/bin/env python3

import requests
import cv2 as cv
import sys
import json

URL = 'http://localhost:9200/test_index/_doc'

def main():
  img_file = sys.argv[1]
  print(f'[+] indexing file {img_file}')
  img = cv.imread(img_file)
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  sift = cv.SIFT_create(50);
  kp, desc = sift.detectAndCompute(img, None)
  print(f'[+] detected {len(kp)} keypoints')
  desc_mat = desc.tolist()
  for i, row in enumerate(desc_mat):
    print(f'\r [+] indexing vector {i+1}/{len(desc_mat)}', end='', flush=True)
    submit_vector(row)
  print()
  print('[+] done')

def submit_vector(vector: list):
  res = requests.post(URL, json={'test_vec': vector})
  res.raise_for_status()

if __name__ == '__main__':
  main()
