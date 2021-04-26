import requests
import json
import sys

URL = 'http://127.0.0.1:5000/courses'

response = requests.get(URL)
data = response.json()

print(json.dumps(response.json(), indent=4))
print(sys.getsizeof(response), len(json.dumps(response.json()).encode("utf-8")))

for datum in data["courses"]:
    datum['course_name'] = datum['course_name'][::-1]
    datum['avg_marks'] = (100 - datum['avg_marks'])

# print(data)
headers = {'Content-type':'application/json', 'Accept':'application/json'}
response = requests.post(URL, data = json.dumps(data), headers = headers)
print(response)