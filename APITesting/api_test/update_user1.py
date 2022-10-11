import requests

payload = {
    "name": "morpheus",
    "job": "zion resident"
}

response = requests.put("https://reqres.in/api/users/2",data=payload)
json_response = response.json()

# validate name
name = json_response['name']
print(name)
assert name=='morpheus'

# validate job
job = json_response['job']
print(job)
assert job=='zion resident'
# validate updatedAt
updatedAt = json_response['updatedAt']
print(updatedAt)
assert updatedAt!=None


