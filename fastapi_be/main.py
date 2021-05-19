from logging import debug
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from fastapi.middleware.cors import CORSMiddleware
## Custom imports
from stocks import getStocksInfo,getHistoryData #type:ignore

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class Health(BaseModel):
    cluster_name: str
    status: str
    timed_out: Optional[bool] = None
    number_of_nodes: int
    number_of_data_nodes: int
    active_primary_shards: int

class Ticker(BaseModel):
    longName: str
    market: str
    phone: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id,"item_price":item.price}


### My IVE-CVE work
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, index
import requests
import json

@app.get("/health")
def health():
    res = requests.get("http://localhost:9100/_cluster/health?pretty")
    data = dict(res.json())
    # hm.cluster_name = data["cluster_name"]
    # hm.status = data["status"]

    # return res.json()
    return {"cluster": data["cluster_name"],"status":data["status"]}

@app.post("/health/{cluster_name}")
def health(cluster_name:str, health:Health):
    if cluster_name == "chain":
        res = requests.get("http://localhost:9100/_cluster/health?pretty")
        data = dict(res.json())
        health.cluster_name = data["cluster_name"]
        health.status = data["status"]
        health.timed_out = data["timed_out"]
        health.number_of_nodes = data["number_of_nodes"]
        health.number_of_data_nodes = data["number_of_data_nodes"]
        health.active_primary_shards = data["active_primary_shards"]
        return {"cluster":health.cluster_name,**health.dict()}
    elif cluster_name == "inpera":
        res = requests.get("http://localhost:9100/_cluster/health?pretty")
        data = dict(res.json())
        health.cluster_name = data["cluster_name"]
        health.status = data["status"]
        health.timed_out = data["timed_out"]
        health.number_of_nodes = data["number_of_nodes"]
        health.number_of_data_nodes = data["number_of_data_nodes"]
        health.active_primary_shards = data["active_primary_shards"]
        return {**health.dict()}

    # return res.json()
    # return {"cluster": data["cluster_name"],"status":data["status"]}

@app.get("/metrics")
def metrics():
    es = Elasticsearch(["localhost"], port=9100)
    scon = Search(using = es, index = "es_test_upgrade_*")
    # qry = scon.query("query_string", query="nw_device_hostname: test.cisco.com", analyze_wildcard = True) \
    qry = scon.query("query_string", query="route:es_test", analyze_wildcard = True) \
                .filter("range", timestamp = {"gt": "now-30d"}) \
                .execute()
    # qcount = qry.hits.hits[0].to_dict()
    qcount = list(qry.hits.hits)
    # qcount = dict(qry.hits.hits)
    # qcount = qry.hits.total
    # print(qcount)
    # return (json.dumps(qcount))
    return {"test":qcount}


@app.post("/stocks/{ticker}/info")
def stocksInfo(ticker:str, tkr: Ticker):
    stockInfo = getStocksInfo(ticker)
    # print(stockInfo)
    tkr.longName = stockInfo["longName"]
    tkr.market = stockInfo["market"]
    tkr.phone = stockInfo["phone"]
    # return {**stockInfo}
    return {**tkr.dict(),"fullInfo":stockInfo}

@app.post("/stocks/{ticker}/history")
def stocksHistory(ticker:str):
    hist_data = getHistoryData(ticker)
    return {**hist_data}

if __name__ == "__main__":
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True, debug=True)

## Testing functions
# stocks("msft")