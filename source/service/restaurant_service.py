from source.datalayer.repository import restaurant_repository


def get_restaurant(restaurant_id: str):
    return restaurant_repository.get_restaurant(restaurant_id)