from flask import Blueprint, render_template, request, make_response
from emoji import emojize


lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username == '' or password == '':
        error = 'Заполните поле!'
        return render_template(
        'login.html',
        error=error,
        username=username,
        password=password
    )
    else:
        return render_template('login_success.html', username=username)
    

@lab4.route('/lab4/fridge/')
def fridge():
    temp = request.args.get('temperature')
    if temp == '':
        output = 'ОШИБКА: не задана температура'
        return render_template('fridge.html', output=output)
    temp = int(temp)
    if temp < -12:
        output = 'Не удалось установить температуру — слишком низкое значение'
    elif temp > -1:
        output = 'Не удалось установить температуру — слишком высокое значение'
    elif temp >= -12 and temp <= -9:
        temp = str(temp)
        output = 'Установлена температура: ' + temp + ' ' + emojize(':snowflake:' )*3
    elif temp >= -8 and temp <= -5:
        temp = str(temp)
        output = 'Установлена температура: ' + temp + ' ' + emojize(':snowflake:' )*2 
    else:
        temp = str(temp)
        output = 'Установлена температура: ' + temp + ' ' + emojize(':snowflake:' )   
    return render_template('fridge.html', output=output, temp=temp)


@lab4.route('/lab4/seed/')
def seed():
    weight = request.args.get('weight')
    type_seed = request.args.get('type_seed')
    if weight == '':
        output = 'Не введен вес'
        return render_template('seed.html', output=output, weight=weight)
    weight = int(weight)
    if weight <= 0:
        output = 'Неверное значение веса'
        return render_template('seed.html', output=output, weight=weight)
    if type_seed == '1':
        summ = 12000 * weight
        type_seed = 'Ячмень'
    elif type_seed == '2':
        summ = 8500 * weight
        type_seed = 'Овёс'
    elif type_seed == '3':
        summ = 8700 * weight
        type_seed = 'Пшеница'
    else:
        summ = 14000 * weight
        type_seed = 'Рожь'
    if weight > 500:
        summ = 'Ошибка'
        output = 'Такого объема сейчас нет в наличии'
        return render_template('seed.html', summ=summ, weight=weight, type_seed=type_seed, output=output)
    elif weight >= 50:
        output = 'За большой объем заказа специально для вас была применена 10% скидка'
        summ = summ-summ/100*10
        return render_template('seed.html', summ=summ, weight=weight, type_seed=type_seed, output=output)
    return render_template('seed.html', summ=summ, weight=weight, type_seed=type_seed) 


@lab4.route('/lab4/cookies/', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')
    
    color = request.form.get('color')
    background_color = request.form.get('background_color')
    size = request.form.get('size')
    if size == '':
        return render_template('cookies.html')
    size = int(size)
    if size >= 5 and size <=30:
        if color != background_color:
            size = str(size)
            response = make_response(render_template('cookies.html', color=color, background_color=background_color, size=size))
            response.set_cookie('background_color', background_color, path='/')
            response.set_cookie('color', color, path='/')
            response.set_cookie('size', size, path='/')
            return response, 303
    return render_template('cookies.html')
 

             