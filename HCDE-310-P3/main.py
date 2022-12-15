from flask import Flask, render_template
from openweather import get_books, get_books_season

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/city/<city>')
def weaterbooks_city(city):
    books = get_books(city)
    return render_template('books.html', books = books)

@app.route('/season/<season>')
def weaterbooks_season(season):
    books = get_books_season(season)
    return render_template('books.html', books = books)

if __name__ == "__main__":
    app.run(debug = True)
