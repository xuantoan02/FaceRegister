import requests
from jose import JWTError, jwt
url = "http://0.0.0.0:8000/protected"

payload = {}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjE2ODY2Mjk2NDV9.PSzA99WcT7F9RgiUZGVtgvn_thhs8nznDg6zqVn753M'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

a=jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjE2ODY2Mjk2NDV9.PSzA99WcT7F9RgiUZGVtgvn_thhs8nznDg6zqVn753M", "123456", algorithms=["HS256"])
z=jwt.encode({'sub': 'adsaa'}, "123456", algorithm="HS256")
print(z)