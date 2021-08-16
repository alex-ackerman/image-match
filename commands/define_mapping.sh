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

echo "[+] creating mapping for $INDEX on $HOST"

curl -s -XPUT \
  -H 'Content-Type: application/json' \
  -d "@mapping.json" \
  "$HOST/$INDEX/_mapping" | jq

echo '[+] done'
