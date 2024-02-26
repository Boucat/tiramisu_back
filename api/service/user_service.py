from fastapi import HTTPException
from fastapi.responses import HTMLResponse

from api.datalayer.repository import user_repository


def display_user(user_id: str):
    user_info = user_repository.get_user(user_id)
    if user_info:
        return HTMLResponse(
            f"<title> Tiramisus de Catalunya </title>"
            f"<h1>{user_info.get('name')}: {user_info.get('description')}</h1> <br>"
            + f"<center> <img src={user_info.get('photo_url')} width='auto' height='50%'> </center>",
            200,
        )
    else:
        return HTTPException(status_code=404, detail=f'User {user_id} not found')
