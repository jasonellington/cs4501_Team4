from elasticsearch import Elasticsearch
import json

es = Elasticsearch(['es'])

with open('db.json') as fixture_file:
	response = fixture_file
	json_obj = json.load(response)

	for i in json_obj:
		if i['model'] == 'models.car':
			make = i['fields']['make']
			car_model = i['fields']['car_model']
			year = i['fields']['year']
			body_type = i['fields']['body_type']
			num_seats = i['fields']['num_seats']
			date_created = i['fields']['date_created']

			some_new_listing = {'make': make, 'car_model': car_model, 'year': year, 'body_type': body_type, 'num_seats': num_seats, 'date_created':date_created, 'id':date_created}

			es.index(index='listing_index', doc_type='listing', id=some_new_listing['id'], body=some_new_listing)

			es.indices.refresh(index="listing_index")




#TODO: In the compose file, for models container, add the command python load_fixtures.py between the loaddata command and the server command