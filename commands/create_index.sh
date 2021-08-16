#!/bin/bash

INDEX='test_index'
HOST='localhost:9200'

if [ ! -z $1 ];
then
  INDEX=$1
fi

if [ ! -z $2 ];
then
  HOST=$2
fi

echo "[+] creating index $INDEX on $HOST"

curl -s -XPUT \
  -H 'Content-Type: application/json' \
  -d '{"settings": {"index":{"number_of_shards": 1, "elastiknn": true}}}' \
  "$HOST/$INDEX" | jq

echo '[+] done'
