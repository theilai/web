import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'CRIM':1, 'RM':3, 'LSTAT':4})

print(r.json())