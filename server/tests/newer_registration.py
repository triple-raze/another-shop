import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import random
from fastapi.testclient import TestClient
from main import app

email = f'user{random.randint(0, 10000000000)}@example.com'

client = TestClient(app)

register_response = client.post('/auth/register/', 
    json={
        "email": email,
        "password": "strg12313112312312",
        "name": "strin1g",
        "gender": "male"
    }
)
print(register_response.status_code, register_response.content)

login_response = client.post('/auth/login/',
    json={
        "email": email,
        "password": "strg12313112312312",
    }
)
print(login_response.status_code, login_response.content)

refresh_response = client.post('/auth/refresh/')
print(refresh_response.content)

delete_response = client.post('/auth/logout/')
print(delete_response.content)
