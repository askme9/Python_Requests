import requests

resp = requests.get("https://reqres.in/api/users?page=2")

#print(resp.text) # returns the content in unicode
#print(resp.content) # returns the content in bytes
print(resp.json()) # Returns the content in json serialize format
print(resp.cookies) # returns the cookies
print(resp.headers) # returns all the headers
print(resp.encoding) # returns the encoded format(Eg: utf-8)
print(resp.url) # returns the url