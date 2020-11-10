from flask import Flask, render_template # подключаем библиблиотеки Flask и Jinja

import data # импортируем файл data.py

app = Flask(__name__) # определяем приложение Flask

@app.route('/')
def main():
    return render_template('index.html') # обработка шаблон для главной страницы

@app.route('/departures/<departute>/')
def departures():
    return render_template('departure.html') # обработка шаблона для направлений

@app.route('/tours/<id>/')
def tours():
    return render_template('tour.html') # обработка шаблон для туров

@app.route('/data/')
def date():
    return render_template('data.html', data=data)

app.run() # запуск сервера Flask