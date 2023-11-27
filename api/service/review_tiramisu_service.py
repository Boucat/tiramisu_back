from api.datalayer.repository import review_tiramisu_repository


def get_all_reviews():
    return review_tiramisu_repository.get_all_reviews()


def get_all_reviews_by_user_id(user_id: str):
    return review_tiramisu_repository.get_all_reviews_by_user_id(user_id)


def get_all_reviews_by_restaurant_id(restaurant_id: str):
    return review_tiramisu_repository.get_all_reviews_by_restaurant_id(restaurant_id)


def create_review():
    return review_tiramisu_repository.create_review()