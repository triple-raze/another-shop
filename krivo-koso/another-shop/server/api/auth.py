from tools.database import execsql
from tools.jwt import JWTService
from tools.hashing import HashService
from models.model_user import UserLogin, UserRegistration
from models.model_jwt import JWTModel

from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post('/auth/register')
async def register_account(user: UserRegistration):

    # hashing passwd
    user.password = HashService.hash(user.password)

    # checking email
    taken_email = await execsql('SELECT EXISTS(SELECT * FROM users WHERE email = $1)', (user.email,), first=True)

    if taken_email['exists']:
        return JSONResponse({'detail': 'This email is taken by another user.'}, status_code=400)

    # creating new user
    await execsql('INSERT INTO users (name, gender, email, password) VALUES ($1, $2, $3, $4)', (user.name, user.gender, user.email, user.password))

    # jsonresponse
    response = JSONResponse({'detail': 'Success'}, status_code=201)

    return response


@router.post('/auth/login')
async def login_account(user: UserLogin, response: Response):

    # checking email
    account_data = await execsql('SELECT * FROM users WHERE email = $1', (user.email,), first=True)

    if not account_data:
        return JSONResponse({'detail': 'Wrong email or password, try again'}, status_code=400)
    
    # validating passwd
    if not HashService.check(user.password, account_data['password']):
        return JSONResponse({'detail': 'Wrong email or password, try again'}, status_code=400)

    # tokens (access and refresh)
    access_token = JWTService.create_token(user.email, 60*15)
    refresh_token = JWTService.create_token(user.email, 60*60*24*14)  # 2 weeks

    # inserting refresh tokens into db
    await execsql('INSERT INTO jwt (refresh_token) VALUES ($1)', (refresh_token,))

    # jsonresponse
    response = JSONResponse({'detail': 'Created refresh and access tokens'}, status_code=200)

    # cookies
    response.set_cookie(
        key = 'access_token',
        value = access_token,
        max_age = 60*15,
        #secure = True,
        httponly = True
    )

    response.set_cookie(
        key = 'refresh_token',
        value = refresh_token,
        max_age = 60*60*24*14,
        #secure = True,
        httponly = True
    )

    return response


@router.post('/auth/logout')
async def logout_account(request: Request, response: Response):

    # getting refresh token from cookies
    refresh_token = request.cookies.get('refresh_token')

    # checking refresh token
    if not refresh_token:
        return JSONResponse({'detail': 'No refresh token found'}, status_code=400)
    
    # deleting refresh token from db
    await execsql('DELETE FROM jwt WHERE refresh_token = $1', (refresh_token,))

    # jsonresponse
    response = JSONResponse({'detail': 'Deleted refresh and access tokens'}, status_code=200)

    # deleting tokens from cookies
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')

    return response


@router.post('/auth/refresh')
async def generate_refresh_token(request: Request, response: Response):

    refresh_token = request.cookies.get('refresh_token')

    # checking refresh token
    old_tokens = await execsql('SELECT refresh_token FROM jwt WHERE refresh_token = $1', (refresh_token,), first=True)
    old_token = old_tokens.get('refresh_token')

    if not old_token:
        return JSONResponse({'detail': 'Token isnt found'}, status_code=404)

    # validating token 
    decoded_old_token = JWTService.decode_token(old_token)
    
    if isinstance(decoded_old_token, Exception):
        return JSONResponse({'detail': str(decoded_old_token)}, status_code=403)
    
    # deleting old token
    await execsql('DELETE FROM jwt WHERE refresh_token = $1', (refresh_token,))

    # creating new token
    new_token = JWTService.create_token(decoded_old_token['sub'], 60*60*24*14)
    
    # adding new token
    await execsql('INSERT INTO jwt (refresh_token) VALUES ($1)', (new_token,))

    # jsonresponse
    response = JSONResponse({'detail': 'Success'}, status_code=200)

    # overriding new cookie
    response.delete_cookie('refresh_token')

    response.set_cookie(
        key = 'refresh_token',
        value = refresh_token,
        max_age = 60*60*24*14,
        #secure = True,
        httponly = True
    )

    return response

