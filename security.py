import datetime
import os
from fastapi import Form, Header, HTTPException
from jose import JWTError
from settings import X_TOKEN, X_KEY
from passlib.context import CryptContext
from typing import Any, Union

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
SECRET_KEY = os.getenv('SECRET_KEY', 'sadasddsadsasad')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS512')
ACCESS_TOKEN_EXPIRE_HOURS = 24

async def verify_token(x_token: str = Header()):
  if x_token != X_TOKEN:
    raise HTTPException(status_code=400, detail="X-Token header invalid")

async def verify_key(x_key: str = Header()):
  if x_key != X_KEY:
    raise HTTPException(status_code=400, detail="X-Key header invalid")
  return x_key

def verify_password(plain_password: str, password: str) -> bool:
    return pwd_context.verify(plain_password, password)

def criar_token_jwt(subject: Union[str, Any]) -> str:
    expire = datetime.utcnow() + datetime.timedelta(
        hours=ACCESS_TOKEN_EXPIRE_HOURS
    )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = JWTError.encode(to_encode, SECRET_KEY, algorithm="HS512")
    return encoded_jwt