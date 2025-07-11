from tools.database import execsql
from models.user import UserForm

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post('/register')
async def register_account(user: UserForm):

    taken_email = await execsql('SELECT EXISTS(SELECT * FROM users WHERE email = $1)', (user.email,), first=True)

    if taken_email['exists']:
        return JSONResponse({'detail': 'This email is taken by another user.'}, status_code=409)
    
    await execsql('INSERT INTO users (name, gender, email, password) VALUES ($1, $2, $3, $4)', (user.name, user.gender, user.email, user.password))
    
    return JSONResponse({'status': 'success'}, status_code=201)
    

@router.post('/login')
async def login_account(user: UserForm):

    account_data = await execsql('SELECT EXISTS(SELECT * FROM users WHERE email = $1 AND password = $2)', (user.email, user.password), first=True)

    if not account_data['exists']:
        return JSONResponse({'detail': 'Wrong email or password, try again'}, status_code=409)
    
