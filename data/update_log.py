from kafka import KafkaConsumer
import json

retry = True

while retry:
    try:
        consumer = KafkaConsumer('popular-items', group_id='popular-items-indexer', bootstrap_servers=['kafka:9092'])
    except:
        print("Exception. Retrying..")
    else:
        retry = False

for message in consumer:
    item_viewed = json.loads((message.value).decode('utf-8'))
    f = open('data/access.log', 'a')
    f.write(item_viewed['user_id'])
    f.write('\t')
    f.write(item_viewed['car_id'])
    f.write('\n')

f.close()
