from .. import app
from flask import jsonify, request
import requests
from os import getenv

@app.get("/weather/<city>/<forecast_type>")
def weather(city: str, forecast_type: str = "weather"):
    api_key = getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/{forecast_type}?q={city}&appid={api_key}&units=metric&lang=ua"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)