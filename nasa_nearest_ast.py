
from os import name
import requests
import json
import pprint
pp=pprint.PrettyPrinter(indent=2, width=10)

API_key="1qjUW09mbVw65Ph7S0CYTgxHlVvYUpgD3qKLgVfX"
START_DATE="2021-02-15"
END_DATE="2021-02-16"


res=requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date="+START_DATE+"&end_date="+END_DATE+"&api_key="+API_key)
data=json.loads(res.text)
data1=data['near_earth_objects']['2021-02-15'][0]
pp.pprint(data1['name'])
