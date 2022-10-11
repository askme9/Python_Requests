import json

import requests

data1 = open('data.json','r').read()

resp = requests.post("https://reqres.in/api/users",data=json.loads(data1))
print(resp)
json_response = resp.json()
print(json_response)

# validate job
job = json_response['job']
print(job)

# validate  headers
print(resp.headers)
#validate content-type
content_type = resp.headers.get("Content-Type")
print(content_type)


