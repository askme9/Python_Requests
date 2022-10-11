import requests
payload = {
    "name": "mukesh",
    "job": "automation"
}

response = requests.patch("https://reqres.in/api/users/2",data=payload)
json_response = response.json()
print(json_response)

# validate name
print(json_response['name'])
assert json_response['name']=='mukesh'

# validate job
print(json_response['job'])
assert json_response['job']=='automation'

# validate updatedAt
print(json_response['updatedAt'])
assert json_response['updatedAt']!=None
