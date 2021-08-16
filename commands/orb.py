#!/usr/bin/env python3

import requests
import cv2 as cv
import sys
import json
import time

def main():
  img_file = sys.argv[1]
  print(f'[+] indexing file {img_file}')
  img = cv.imread(img_file)
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  feature_extractor = cv.ORB_create(50);
  # feature_extractor = cv.SIFT_create(50);
  start = time.perf_counter()
  kp, desc = feature_extractor.detectAndCompute(img, None)
  end = time.perf_counter()
  print(f'[+] detected {len(kp)} keypoints in {(end-start) * 1000}ms.')
  desc_mat = desc.tolist()
  print(len(desc_mat[0]))
  print(desc_mat[0])
  # for i, row in enumerate(desc_mat):
  #   print(row)
  print()
  print('[+] done')

if __name__ == '__main__':
  main()
