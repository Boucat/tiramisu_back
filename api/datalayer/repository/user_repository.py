import hashlib

from api import USERS


def get_user(user_id: str):
    sec_user = hashlib.sha1(user_id.encode('utf-8')).hexdigest()
    return USERS.get(sec_user)
