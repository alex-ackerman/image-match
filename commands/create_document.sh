#!/bin/bash

DOC_FILE='dense_float_vector_low.json'
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

echo "[+] creating document from file $DOC_FILE for $INDEX on $HOST"

curl -s -XPOST \
  -H 'Content-Type: application/json' \
  -d "@$DOC_FILE" \
  "$HOST/$INDEX/_doc" | jq

echo '[+] done'
