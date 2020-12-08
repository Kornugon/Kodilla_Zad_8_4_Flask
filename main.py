"""
Zadanie 8.4:
Czas na zadanie związane z Flaskiem.

Poprzednio stworzyliśmy już podwaliny Twojej strony-wizytówki. Jeśli chcemy wykorzystać dane z formularza, to potrzebujemy jakiegoś backendu. Potrzebujemy, by coś po drugiej stronie „nasłuchiwało” na dane z formularza.

Dwie strony, które powstały, będą dwoma szablonami Flask. Znajdź wspólną przestrzeń, którą możesz współdzielić – np. wspólny tytuł i obrazek. Ten kontent umieścimy w szablonie bazowym, który możesz dziedziczyć w szablonach dzieciach.

image
Co do backendu, zaprojektuj prostą aplikację z Flask. W sumie musisz zdefiniować trzy funkcje adnotowane @app.route – dwie, które wyświetlą strony i trzecią przeznaczoną dla zapisywania danych z formularza. Oznacz je odpowiednio.

/mypage/me – informacje o mnie
/mypage/contact – informacje kontaktowe
/mypage/contact (POST) – zapis formularza
Kod, który ma wysyłać informację, niech po prostu zapisze tę wiadomość na konsoli.
"""

from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)


#/mypage/me – informacje o mnie 
#oznaczyłęm to jako "about"
#http://localhost:5000/about
@app.route("/about")
def about():
    return render_template("about.html")

#/mypage/contact – informacje kontaktowe
@app.route("/contact")
def contact():
    items = ["email: piotr.loba22@gmail.com", "telefon: +48 111 222 333"]
    return render_template("contact.html", items=items)

#/mypage/contact (POST) – zapis formularza
@app.route('/contact', methods=['POST'])
def post():
    if request.method == 'POST':
        print("We received POST")
        print(request.form)
        return request.form

