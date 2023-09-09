from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <a href='/lab1'>Первая лабораторная</a>

        <footer>
            &copy; Ветрова, Клопенкова, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Ветрова, Клопенкова, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Flask — фреймворк для создания веб-приложений на языке
программирования Python, использующий набор инструментов
Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
называемых микрофреймворков — минималистичных каркасов
веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</h1>

        <footer>
            &copy; Ветрова, Клопенкова, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
"""