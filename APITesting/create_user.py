import requests

#payload
payload = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post("https://reqres.in/api/users",data=payload)
print(response)
json_response = response.json()
print(json_response)

# validate name
name = json_response['name']
print(name)
assert name=='morpheus'

# validate job
job = json_response['job']
print(job)
assert job=='leader'

# validate id
id = json_response['id']
print(id)
assert id!=None

# validate createdAt
createdAt = json_response['createdAt']
assert createdAt!=None


