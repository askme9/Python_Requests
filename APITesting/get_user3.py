
import requests

p = {"page":2}
response = requests.get("https://reqres.in/api/users?",params=p)
print(response)

# to check the url passed with the get request is same as earlier url

url = response.url
print(url)

json_response = response.json()