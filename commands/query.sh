#!/bin/bash

DOC_FILE='query_vector.json'
INDEX='test_index'
HOST='localhost:9200'

if [ ! -z $1 ];
then
  DOC_FILE=$1
fi

if [ ! -z $2 ];
then
  INDEX=$2
fi

if [ ! -z $3 ];
then
  HOST=$3
fi

echo "[+] querying index $INDEX on $HOST with contents of $DOC_FILE"

curl -s -XGET \
  -H 'Content-Type: application/json' \
  -d "@$DOC_FILE" \
  "$HOST/$INDEX/_search" | jq

echo '[+] done'
