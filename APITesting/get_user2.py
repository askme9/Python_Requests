import requests

resp = requests.get("https://reqres.in/api/users?page=2")
json_response = resp.json()
print(json_response)
# validate total_pages
total_pages = json_response['total_pages']
print(total_pages)
assert total_pages==2,"total_pages count is not matched"

# validate total
total = json_response['total']
print(total)
assert total==12

# validate email of the first record inside data

email1 = json_response['data'][0]['email']
print(email1)

# validate the email is ending with reqres.in
assert email1.endswith('reqres.in')

# validate first name
firstname1 = json_response['data'][0]['first_name']
print(firstname1)

assert firstname1,'Michael'

# validate last name of 5th record
last_name5 = json_response['data'][4]['last_name']
print(last_name5)
assert last_name5!=None

# validate text from 'support' node

support_text = json_response['support']['text']
print(support_text)




