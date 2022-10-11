import requests

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.post("https://reqres.in/api/register",data=payload)
print(response)

json_response = response.json()
print(json_response)

# validate token
token = json_response.get('token')
print(token)

assert token!=None