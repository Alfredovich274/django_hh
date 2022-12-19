import requests
import pprint

    # "cities": "http://127.0.0.1:8000/api/v0/cities/",
    # "skills": "http://127.0.0.1:8000/api/v0/skills/",
    # "params": "http://127.0.0.1:8000/api/v0/params/",
    # "experience": "http://127.0.0.1:8000/api/v0/experience/"

# response = requests.get('http://127.0.0.1:8000/api/v0/params/')
# pprint.pprint(response.json())

token = '0098a1cda1fbf9133008b8b4979f674d1291f241'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/experience/', headers=headers)
# response = requests.get('http://127.0.0.1:8000/api/v0/experience/')
pprint.pprint(response.json())
