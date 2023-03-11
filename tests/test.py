import requests
import json

url = 'http://localhost:8000/house_price_prediction'

data = {
    'area_income': 44.9,
    'house_age': 44.99,
    'number_of_rooms': 55.99,
    'number_of_bed_rooms': 33.55,
    'area_population': 55.55
}

headers = {
    'Content-type': 'application/json',
    'Accept': 'text/plain'
}
data1=json.dumps(data)
print(data1)
print(type(data))
print(type(data1))
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)
