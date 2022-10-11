import requests

# The response time is 10 seconds, you had given the timeout as 5 seconds. That means, if we are not getting the response in 5 seconds, it will not wait and fail
resp = requests.get("https://httpbin.org/delay/5",timeout = 10)
print(resp.status_code)

