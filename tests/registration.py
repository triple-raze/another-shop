import requests

response = requests.post(
    'http://127.0.0.1:8000/api/register',
    json={
        'name': 'sanek',
        'gender': 'male',
        'email': 'zxccevyavlov@gmail.com',
        'password': 'rukobludd228'
    }
)

print(f'{response}\n{response.text}')   # false


response = requests.post(
    'http://127.0.0.1:8000/api/register',
    json={
        'name': 'alex epta',
        'gender': 'male',
        'email': 'alex.johnson@example.com',
        'password': 'megahuesos228'
    }
)

print(f'{response}\n{response.text}')   # true


response = requests.post(
    'http://127.0.0.1:8000/api/register',
    json={
        'name': 'karen',
        'gender': 'non-binary',
        'email': 'feministka@example.com',
        'password': 'sozxcyzxczxi2123'
    }
)

print(f'{response}\n{response.text}')   # non-binary isnt a thing