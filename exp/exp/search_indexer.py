from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import time
import json

time.sleep(20)

retry = True

while retry:
    try:
        es = Elasticsearch(['es'])
        consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
    except:
        print "Exception. Retrying.."
    else:
        retry = False

while True:
    for message in consumer:
        new_listing = json.loads((message.value).decode('utf-8'))
        es.index(index='listing_index', doc_type='listing', id=new_listing['id'], body=new_listing)
    es.indices.refresh(index="listing_index")
    time.sleep(0.5)
