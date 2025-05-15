from fastapi import HTTPException, status


EMAIL_ALREADY_REGISTERED =  HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

INCORRECT_EMAIL_OR_PASSWORD = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect email or password')

EXPIRED_JWT_TOKEN = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token has expired', headers={"WWW-Authenticate": "Bearer"})

INVALID_JWT_TOKEN = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token', headers={"WWW-Authenticate": "Bearer"})