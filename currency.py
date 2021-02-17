
import requests
import json
import pprint

pp=pprint.PrettyPrinter(indent=2, width=10)

API_key="6fa58852246440c5b7b635f8cdbd8f86"
currency="USD"

res=requests.get("http://data.fixer.io/api/latest?access_key="+API_key+"&symbols=MDL")
data=json.loads(res.text)
pp.pprint(data)