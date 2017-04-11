from elasticsearch import Elasticsearch
import json
from .models import Car


retry = True

while retry:
    try:
		es = Elasticsearch(['es'])
    except:
        print("Exception. Retrying..")
    else:
        retry = False

with open('db.json') as fixture_file:
	response = fixture_file
	json_obj = json.load(response)

	for i in json_obj:
		if i['model'] == 'models.car':
			date_created = i['fields']['date_created']

			car = Car.objects.get(date_created=date_created)

			new_listing = {'make': car.make, 'car_model': car.car_model, 'year': car.year, 'body_type': car.body_type, 'num_seats': car.num_seats, 'date_created':car.date_created, 'id':car.id}

			es.index(index='listing_index', doc_type='listing', id=new_listing['id'], body=new_listing)

es.indices.refresh(index="listing_index")
