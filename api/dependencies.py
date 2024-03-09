import hashlib

from fastapi import HTTPException, Query

from api import USER_MOCK_DB


async def check_user_token(user_id: str = Query(..., title='User', description='The user parameter')):
    hashed_token = hashlib.sha1(user_id.encode('utf-8')).hexdigest()
    hashed_tokens_db = [token.get('sec_key') for token in USER_MOCK_DB]
    if hashed_token in hashed_tokens_db:
        return user_id, hashed_token
    else:
        raise HTTPException(status_code=401, detail='Wrong token provided')
