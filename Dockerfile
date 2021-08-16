FROM docker.elastic.co/elasticsearch/elasticsearch:7.13.3

RUN elasticsearch-plugin install --batch https://github.com/alexklibisz/elastiknn/releases/download/7.13.3.1/elastiknn-7.13.3.1.zip
