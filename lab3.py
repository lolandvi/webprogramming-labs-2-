from flask import Blueprint, render_template, request


lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1/')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template(
        'form1.html',
        user=user,
        age=age,
        sex=sex,
        errors = errors
    )


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
        age = '18'
    age1 = int(age)
    if (age1 < 18) or (age1 > 120):
        errors['age1'] = 'Ваш возраст не подходит'
    from1 = request.args.get('from1')
    if from1 == '':
        errors['from1'] = 'Заполните поле!'
    where = request.args.get('where')
    if where == '':
        errors['where'] = 'Заполните поле!'
    datetime = request.args.get('datetime')
    if datetime == '':
        errors['datetime'] = 'Заполните поле!'
    place = request.args.get('place')
    if place == '1':
        place_output = 'Нижняя полка'
    elif place == '2':
        place_output = 'Верхняя полка'
    elif place == '3':
        place_output = 'Боковая нижняя полка'
    else:
        place_output = 'Боковая верхняя полка'
    return render_template(
        'ticket.html',
        user=user,
        from1=from1,
        where=where,
        datetime=datetime,
        age=age,
        age1=age1,
        place_output=place_output,
        place=place,
        errors = errors
    )


