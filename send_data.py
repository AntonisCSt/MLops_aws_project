import json
import uuid
from time import sleep
from datetime import datetime
import requests
from pyarrow import csv

table = csv.read_csv("sample.csv")
data = table.to_pylist()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


with open("target.csv", 'w') as f_target:
    
    for row in data:
        data=json.dumps(row, cls=DateTimeEncoder)
        #print(row)
        resp = requests.post(
            "http://127.0.0.1:9696/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(row, cls=DateTimeEncoder),
        ).json()
        print(f"prediction: {resp['Fire Alarm']}")
        sleep(0.2)

        #http://127.0.0.1:9696/predict