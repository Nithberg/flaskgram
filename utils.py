import json

# Константа для файла с постами
DATA_OF_POSTS = 'data/posts.json'
DATA_OF_COMMENTS = 'data/comments.json'


def get_posts_all():
    '''
    Функция загрузки данных постов из posts.json
    :return: возращает все посты для отрисовки в вьюшке main
    '''
    with open(DATA_OF_POSTS, 'r', encoding='utf-8') as file:
        all_posts = json.load(file)
    return all_posts


def get_post_by_pk(pk):
    return [post for post in get_posts_all() if pk == post['pk']]


def get_comments_by_post_id(post_id):
    with open(DATA_OF_COMMENTS, 'r', encoding='utf-8') as file:
        all_comments = json.load(file)
    return [comment for comment in all_comments if post_id == comment['post_id']]


def search_for_posts(query):
    return [post for post in get_posts_all() if query in post['content']]

def get_posts_by_user(user_name):
    return [post for post in get_posts_all() if user_name in post['poster_name']]


