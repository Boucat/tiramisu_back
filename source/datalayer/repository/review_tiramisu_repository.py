def get_all_reviews():
    return {"title": "The great Plumbus"}


def get_all_reviews_by_user_id(user_id: str):
    return [{"title": "The great Plumbus", "user_id": user_id}]


def get_all_reviews_by_restaurant_id(restaurant_id: str):
    return [{"title": "The great Plumbus", "restaurant_id": restaurant_id}]


def create_review():
    return {"restaurant_id": "Restaurant id", "name": "The great Plumbus"}