#!/usr/bin/env python3

import requests
import cv2 as cv
import sys
import json
import time

URL = 'http://localhost:9200/test_index/_search'

def main():
  img_file = sys.argv[1]
  print(f'[+] querying features from {img_file}')
  img = cv.imread(img_file)
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  # extractor = cv.SIFT_create(50);
  extractor = cv.ORB_create(50);
  start = time.perf_counter()
  kp, desc = extractor.detectAndCompute(img, None)
  end = time.perf_counter()
  print(f'[+] detected {len(kp)} keypoints in {(end - start) * 1000}ms.')
  desc_mat = desc.tolist()
  results = []
  
  start = time.perf_counter()
  for i, row in enumerate(desc_mat):
    print(f'\r [+] matching vector {i+1}/{len(desc_mat)}', end='', flush=True)
    res = query(row)
    results.append(res)
  print()
  end = time.perf_counter()
  print(f'[+] done in {(end - start) * 1000}ms.')
  # print(json.dumps(results[0]))
  for result in results:
    print(result.get('hits').get('hits')[0].get('_source').get('title'))

def query_body(vector: list) -> dict:
  return {
    "from": 0,
    "size": 1,
    "query": {
      "elastiknn_nearest_neighbors": {
        "field": "image_vec",
        "vec": {
          "values": vector
        },
        "model": "lsh",
        "similarity": "cosine",
        "candidates": 1
      }
    }
  }

def query(vector: list):
  res = requests.get(URL, json=query_body(vector))
  if not res.ok:
    print(res.json())
  return res.json()

def submit_vector(vector: list):
  res = requests.post(URL, json={'test_vec': vector})
  res.raise_for_status()

if __name__ == '__main__':
  main()
