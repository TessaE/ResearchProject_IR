##########################
# Indexing and searching
##########################


from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json


es = Elasticsearch()
ind = 'products'
source_file = 'fullscrape.txt'

import sys
print(sys.version_info)

def createIndex():
    if es.indices.exists(ind):
        print(ind + ' exists')
    else:
       with open(source_file, 'r', encoding="utf8") as jsonfile:
            
            
            # Create index with settings
            print('Creating index...')
            request_body = {
                "settings": {
                    "number_of_shards": 5,
                    "number_of_replicas": 0
                }
            }
            
            res = es.indices.create(index=ind, body=request_body, request_timeout=30)
            
            actions = []
            for row in jsonfile:
                data = json.loads(row)
                
                action = {
                    "_index": ind,
                    "_type": "product",
                    "_id": data["pid"],
                    "_source": {
                        "pid": data['pid'],
                        "name": data['name'],
                        "brand": data['brand'],
                        "description": data['description'],
                        "long_description": data['long_description'],
                        "image_urls": data['image_urls'],
                        "keywords": data['keywords'],
                        "source_categories": data['source_categories'],
                        "original_url": data['original_url'],
                        "canonical_url": data['canonical_url'],
                        "breadcrumbs": data['breadcrumbs'],
                        "price": data['price']
                        }
                    }
                actions.append(action)



            if len(actions) > 0:
                helpers.bulk(es, actions, chunk_size=5000, refresh =True)
            es.indices.put_settings(index=ind, body={"number_of_replicas": 0})
            print('Indexing finished.')
        

def deleteIndex():
    print('Deleting index...')
    return es.indices.delete(index=ind, ignore=[400, 404])


def search(searchbody):
    res = es.search(index=ind, body=searchbody)
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print(str(hit['_source']['pid']) + ': ' + hit['_source']['name'])



#deleteIndex()
#createIndex()
search({
    "from": 0, "size": 100,
    "query": {
        "match": {
            "_all": "brandweerauto"
        }
    }
})






