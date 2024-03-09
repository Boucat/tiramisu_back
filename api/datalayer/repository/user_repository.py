import hashlib

from api import USER_MOCK_DB


def get_user(user_id: str):
    sec_user = hashlib.sha1(user_id.encode('utf-8')).hexdigest()
    return USER_MOCK_DB.get(sec_user)
