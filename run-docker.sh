#!/bin/bash

docker run -it --rm -p9200:9200 -p9300:9300 -e 'discovery.type=single-node' elastiknn-example
