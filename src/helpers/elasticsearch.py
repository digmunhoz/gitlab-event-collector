import logging
from settings import Settings
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class CustomElasticsearch:
    def client(self):
        return Elasticsearch([Settings.ELASTICSEARCH_ADDRESS])

    def insert_data(self, doc, index_prefix, index_suffix):
        es = self.client()
        es_index = f"{index_prefix}{index_suffix}"
        for item in doc:
            item.update({"insertion_timestamp": datetime.utcnow()})
            if item.get("id"):
                item.update({"_id": item.get("id")})
        bulk(es, doc, index=es_index)
