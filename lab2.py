from flask import Blueprint, render_template


lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
def example():
    name = 'Ветрова Лолита, Клопенкова Виктория'
    number = '2'
    group = 'ФБИ-11'
    curs = '3'
    fruits = [
        {'name': 'Яблоки', 'price': 100},
        {'name': 'Груши', 'price': 120},
        {'name': 'Апельсины', 'price': 80},
        {'name': 'Мандарины', 'price': 95},
        {'name': 'Манго', 'price': 321}
    ]
    books = [
        {'name': 'Книга 1', 'author': 'Автор 1', 'theme': 'Жанр 1', 'page': 100},
        {'name': 'Книга 2', 'author': 'Автор 2', 'theme': 'Жанр 2', 'page': 200},
        {'name': 'Книга 3', 'author': 'Автор 3', 'theme': 'Жанр 3', 'page': 300},
        {'name': 'Книга 4', 'author': 'Автор 4', 'theme': 'Жанр 4', 'page': 400},
        {'name': 'Книга 5', 'author': 'Автор 5', 'theme': 'Жанр 5', 'page': 500},
        {'name': 'Книга 6', 'author': 'Автор 6', 'theme': 'Жанр 6', 'page': 600},
        {'name': 'Книга 7', 'author': 'Автор 7', 'theme': 'Жанр 7', 'page': 700},
        {'name': 'Книга 8', 'author': 'Автор 8', 'theme': 'Жанр 8', 'page': 800},
        {'name': 'Книга 9', 'author': 'Автор 9', 'theme': 'Жанр 9', 'page': 900},
        {'name': 'Книга 10', 'author': 'Автор 10', 'theme': 'Жанр 10', 'page': 1000},
    ]
    return render_template(
        'example.html', 
        name=name, 
        number=number, 
        group=group, 
        curs=curs, 
        fruits=fruits,
        books=books
    )


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/cats')
def cats():
    return render_template('cats.html')
