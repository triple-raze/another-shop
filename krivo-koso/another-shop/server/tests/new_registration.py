import random
import requests

email = f'user{random.randint(0, 10000000000)}@example.com'

with requests.Session() as session:
    
    register_response = session.post('http://127.0.0.1:8000/auth/register', 
        json={
            "email": email,
            "password": "strg12313112312312",
            "name": "strin1g",
            "gender": "male"
        }
    )
    print(register_response.status_code, register_response.content)

    login_response = session.post('http://127.0.0.1:8000/auth/login',
        json={
            "email": email,
            "password": "strg12313112312312",
        }
    )
    print(login_response.status_code, login_response.content)

    
    cookies = login_response.cookies.get_dict()

    print(cookies, login_response.headers)

