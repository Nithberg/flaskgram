from flask import Blueprint, render_template, request, abort
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

'''
Создание блюпринта main
Определение директории для статики - static_folder='static'
Определение директории для шаблонов - template_folder='templates'
'''
main_blueprint = Blueprint('main', __name__, static_folder='static', static_url_path='/', template_folder='templates')


# Создание вьюшки главной страницы index.html
@main_blueprint.route('/')
def main():
    all_posts = get_posts_all()
    return render_template('index.html', all_posts=all_posts)


@main_blueprint.route('/posts/<int:postid>')
def post(postid):
    if postid > len(get_posts_all()):
        return abort(404)
    else:
        view_post = get_post_by_pk(postid)
        view_comments = get_comments_by_post_id(postid)
        return render_template('post.html', view_post=view_post, view_comments=view_comments,
                               amount_of_comments=len(view_comments))


@main_blueprint.route('/search', methods=['GET'])
def search_post():
    search = request.args['s']
    view_post = search_for_posts(search)
    return render_template('search.html', view_post=view_post, search=search, amount_of_posts=len(view_post))


@main_blueprint.route('/users/<user_name>')
def posts_by_username(user_name):
    view_user_posts = get_posts_by_user(user_name)
    view_username = user_name
    return render_template('user-feed.html', view_user_posts=view_user_posts, view_username=view_username)
