from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
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

        <h1>web-server on the flask</h1>

        <footer>
            &copy; Ветрова, Клопенкова, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
"""