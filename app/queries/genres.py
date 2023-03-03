from peewee import IntegrityError, DoesNotExist
from app.models.posts.post_model import Genre
from app.models.basemodel import db

@db
def create_genre(title: str):
    try:
        obj = Genre.create(title=title)
    except IntegrityError:
        obj = 0
    return obj



@db
def delete_genre(title: str):
    try:
        genre = Genre.get(title=title)
        # SELEC * FROM genre WHERE title = title
        genre.delete_instance()
    except DoesNotExist:
        return 0
    return 1

@db
def get_genres():
    return [genre.title for genre in Genre.select()]


