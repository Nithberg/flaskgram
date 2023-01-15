from flask import Flask, Blueprint
from main.main import main_blueprint

app = Flask(__name__)

# Регистрация блюпринта main
app.register_blueprint(main_blueprint)

@app.errorhandler(404)
def page_not_found(e):
    e = 404
    return f'<h2>ОШИБКА {e}! Такой страницы не существует</h2>'
@app.errorhandler(500)
def page_not_found(e):
    e = 500
    return f'<h2>ОШИБКА {e}! Что-то пошло не так!</h2>'


if __name__ == '__main__':
    app.run()
