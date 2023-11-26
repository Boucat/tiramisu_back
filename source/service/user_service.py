from source.datalayer.repository import user_repository

def get_user(user_id: str):
    return user_repository.get_user(user_id)