from flask import Blueprint, render_template, request
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
    