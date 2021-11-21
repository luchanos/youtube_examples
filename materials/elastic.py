from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()

doc = {
    # "created": datetime.now(),
    "description": "Типовой документ",
    "in_stock": 10000,
    "is_active": False,
    "name": "типовое имя"
}

# res = es.index(index="products", document=doc)
res_1 = es.search(index="products", body={
    "query": {
        "match": {
            "name": "типовое имя"
        }
    }
})
c = 1
