from app.models.posts.post_model import Post, PostGenres, Genre
from app.models.basemodel import db
from datetime import date
from typing import List
from peewee import fn

@db
def create_post(
    title: str,
    description: str,
    year: date,
    country: str,
    genres: List[str]) -> Post:
    post = Post.create(
        title=title,
        description=description,
        year=year,
        country=country,
        )
    for genre in genres:
        g = Genre.get(title=genre)
        post.genre.add(g)
    return post


@db
def get_all_films():
    posts = Post.select(Post.id, Post.title, Post.year)
    # SELECT title, year FROM post;
    return [{'id': post.id, 'title': post.title, 'year': post.year} for post in posts]


@db
def get_film_by_id(id):
    post = Post.select(Post, fn.array_agg(Genre.title).alias('genre_titles')).join(PostGenres).join(Genre).where(Post.id == id).group_by(Post.id).get_or_none()
    return {
        'id': post.id,
        'title': post.title,
        'description': post.description,
        'year': post.year,
        'county': post.country,
        'genres': [genre.title for genre in post.genre]
    }

# TODO: дописать CRUD для модели Posts
# TODO: Прочитать документацию FastApi htttps://fastapi.tiangolo.com/