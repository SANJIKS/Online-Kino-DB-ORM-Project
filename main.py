from app.models.posts.post_model import Genre, Post, PostGenres
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, get_all_films, get_film_by_id
@db
def create_tables() -> None:
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()

create_genre('Детектив')
create_genre('Фантастика')
create_genre('Наука')
create_genre('Экшен')
create_genre('Боевик')
create_genre('Ужасы')

# delete_genre('Детектив')

# print(get_genres())

# create_post('Человек муравей и Оса: Квантомания', "ыпыпыпыпы", '2023', 'USA', ['Фантастика', 'Наука', 'Экшен', 'Боевик'])
# create_post('Разбой', "жоский", "2023", 'Kyrgyzstan', ['Боевик', "Экшен", "Детектив"])
print(get_all_films(), f"\n")
print(get_film_by_id(2))