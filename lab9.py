from flask import Blueprint, render_template, request

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(err):
    return render_template('lab9/404.html')

@lab9.app_errorhandler(500)
def not_found(err):
    return render_template('lab9/500.html')

@lab9.route('/lab9/500')
def main_500():
    raise Exception("Ошибка 500: сервер сломался!")


@lab9.route('/lab9/new_year_card')
def new_year_card():
    recipient_name = request.args.get('recipient_name', '')
    recipient_gender = request.args.get('recipient_gender', '')
    sender_name = request.args.get('sender_name', '')

    if recipient_name and sender_name:
        if recipient_gender == 'male':
            message = f"С Новым годом, дорогой {recipient_name}! Желаю быть счастливым в новом году! Отправитель: {sender_name}"
        elif recipient_gender == 'female':
            message = f"С Новым годом, дорогая {recipient_name}! Желаю быть счастливой в новом году! Отправитель: {sender_name}"
        else:
            message = "Неверно указан пол получателя"
    else:
        message = ""

    return render_template('lab9/new_year_card.html', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name, message=message)