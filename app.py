from flask import Flask, render_template # подключаем библиблиотеки Flask и Jinja

import data # импортируем файл data.py

app = Flask(__name__) # определяем приложение Flask

@app.route('/')
def main():
    return render_template('index.html', data=data) # обработка шаблон для главной страницы

@app.route('/departures/<departure>/')
def departures(departure):
    return render_template('departure.html', data=data, departure=departure) # обработка шаблона для направлений

@app.route('/tours/<int:id>/')
def tour(id):
    tour = data.tours[id]
    return render_template('tour.html', data=data, id=id, tour=tour) # обработка шаблон для туров

@app.route('/data/')
def date():
    return render_template('data.html', data=data)

app.run() # запуск сервера Flask