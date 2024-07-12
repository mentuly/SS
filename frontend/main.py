from os import getenv
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
import requests

load_dotenv()

app = Flask(__name__)

# Маршрути
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "login"
    return render_template("login.html")

@app.route("/logout")
def logout():
    return "logout"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return "register"
    return render_template("register.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/weather/<city>/<forecast_type>")
def weather(city: str, forecast_type: str = "weather"):
    api_key = getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/{forecast_type}?q={city}&appid={api_key}&units=metric&lang=ua"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

# Обробники помилок
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.errorhandler(ValueError)
def value_error_exception_handler(error: ValueError):
    return f'Value error {str(error)}'

@app.errorhandler(KeyError)
def key_error_exception_handler(error: KeyError):
    return f'Key error {str(error)}'

if __name__ == "__main__":
    debug = getenv("DEBUG", "1")
    port = getenv("PORT", "5000")
    app.run(debug=int(debug), port=int(port))