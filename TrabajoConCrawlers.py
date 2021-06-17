import requests

miReq=requests.get("https://www.movistar.es")
print(miReq.status_code)
print(miReq.headers)
print(miReq.text)