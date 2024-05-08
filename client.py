import requests

endpoint = 'http://localhost:5001/predict_v1/32/10000'
response = requests.get(endpoint)
print ("predict v1", response.json())


endpoint = 'http://localhost:5001/predict_v2?age=32&salary=10000'
response = requests.get(endpoint)
print ("predict v2", response.json())


endpoint = 'http://localhost:5001/predict_v3'
args = {'age': 41, 'salary': 23000 }
response = requests.post(endpoint, json=args)
print ("predict v3", response.json())


