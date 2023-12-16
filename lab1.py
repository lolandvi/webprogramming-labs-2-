from flask import Blueprint, redirect, url_for


lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
def menu():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''"
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <main>
            <br>
            <ol>
            <li><a href='/lab1'>Первая лабораторная работа</a></li>
            <li><a href='/lab2'>Вторая лабораторная работа</a></li>
            <li><a href='/lab3'>Третья лабораторная работа</a></li>
            <li><a href='/lab4'>Четвертая лабораторная работа</a></li>
            <li><a href='/def3?exist=1&full=2'>Защита лабораторная работа</a></li>
            <li><a href='/lab5'>Пятая лабораторная работа</a></li>
            <li><a href='/lab6/head'>Шестая лабораторная работа</a></li>
            <li><a href='/lab7'>Седьмая лабораторная работа</a></li>
            </ol>
        </main>
        <footer>
            &copy; Ветрова, Клопенкова, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
'''


@lab1.route("/lab1")
def lab():
    return '''
<!doctype html>
<html>
    <head>
        <title>Ветрова, Клопенкова, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''"
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <br>
            <div>
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </div>

            <a href='/menu'>Назад к меню</a>

            <h2>Реализованные роуты</h2>
            <ul>
            <li><a href='/lab1/oak'>Дуб</a></li>
            <li><a href='/lab1/student'>Студенты</a></li>
            <li><a href='/lab1/python'>О Python</a></li>
            <li><a href='/lab1/teacher'>Преподаватель</a></li>
            </ul>
        </main>

        <footer>
            &copy; Ветрова, Клопенкова, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
'''


@lab1.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''"
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.png') + '''">
    </body>
</html>    
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>Ветрова, Клопенкова, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''"
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <h1>Ветрова Лолита Алексеевна</h1>
            <h1>Клопенкова Виктория Владимировна</h1>
            <img src="''' + url_for('static', filename='nstu.jpg') + '''">
        </main>
        <footer>
            &copy; Ветрова, Клопенкова, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
'''


@lab1.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <head>
        <title>Ветрова, Клопенкова, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''"
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <h1>О Python</h1>

            <div>
                Создатель языка Python — нидерландский программист Гвидо ван Россум. Он был участником проекта по написанию ABC, 
                языка для обучения программированию. В конце 1989 года Гвидо приступил к разработке нового языка и задумал его как потомка ABC, 
                способного к обработке исключений и взаимодействию с операционной системой Amoeba. Так и получился Python.
            </div>
            <div>
                Специалисты выделяют массу преимуществ Python — остановимся на ключевых из них.<br>
                Простота синтаксиса, а значит — низкий порог вхождения. Код языка чистый и понятный, без лишних символов и выражений.<br>
                Расширяемость и гибкость. Не зря один из слоганов языка — это «Just Import!» Python можно легко расширить для взаимодействия 
                с другими программными системами или встроить в программы в качестве компонента. Он очень и очень гибкий. Это даёт больше возможностей 
                для использования языка в разных сферах.<br>
                Интерпретируемость и кроссплатформенность. Интерпретатор Python есть для всех популярных платформ и по умолчанию входит в 
                большинство дистрибутивов Linux.<br>
                Стандартизированность. У Python есть единый стандарт для написания кода — Python Enhancement Proposal или PEP, благодаря чему язык 
                остаётся читабельным даже при переходе от одного программиста к другому.<br>
                Open Source. У интерпретатора Python открытый код, то есть любой, кто заинтересован в развитии языка, может поучаствовать в его разработке
                и улучшении.<br>
                Сильное комьюнити и конференции. Вокруг Python образовалось дружественное комьюнити, которое готово прийти на помощь новичку или уже
                опытному разработчику и разобраться в его проблеме. Во всём мире проходит много мероприятий, где можно познакомиться с коллегами 
                и узнать много нового о применении Пайтона.<br>
                Широта применения. Наиболее широко Python используется в web-разработке, работе с данными, автоматизации бизнес-процессов и геймдеве.<br>
                Востребованность на рынке труда и поддержка гигантами IT-сферы. Python-разработчики востребованы во многих проектах и им
                несложно найти работу. Разработку на Python ведут в Google, Facebook, Dropbox, Spotify, Quora, Netflix, Microsoft Intel, 
                а в России — «Яндекс», «ВКонтакте» и «Сбербанк». Это серьёзно влияет на статус языка.<br>
            </div>
            <img src="''' + url_for('static', filename='python.jpg') + '''">
        </main>
        <footer>
            &copy; Ветрова, Клопенкова, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
'''


@lab1.route("/lab1/teacher")
def teacher():
    return '''
<!doctype html>
<html>
    <head>
        <title>Ветрова, Клопенкова, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''"
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <h1>Горин Андрей Витальевич</h1>
            <div>
                Стаж в IT - 2 года<br>
                Предмет - Web-программирование, Машинное обучение и нейронные сети
            </div>
            <div>
                Что больше всего вам нравится в преподавании?<br>
                Существуют три закона Кларка. Один из них звучит так: "Любая достаточно развитая технология неотличима от магии". 
                По своему опыту, я не могу с ним не согласиться. Но этот "закон" меня безумно раздражает.
                Когда студент на защите долго и усердно пересказывает очень умными терминами часть работы, но при этом не понимая, 
                какой смысл заключен в этих предложениях, я начинаю задавать ему наводящие вопросы. Он смущается, немного нервничает, а затем, 
                после нескольких кратких пояснений и предложений "порассуждать", следует то долгожданное: "Аааааа, так вот как это работает!"<br>
                И чувство "магии" потихоньку рассеивается в его глазах.
                Вот этот процесс "рассеивания магии" мне очень нравится в жизни и преподавании.
            </div>
            <img src="''' + url_for('static', filename='gorin.png') + '''">
        </main>
        <footer>
            &copy; Ветрова, Клопенкова, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
'''