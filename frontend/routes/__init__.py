from os import getenv
from dotenv import load_dotenv
from flask import Flask
# from flask_mail import Mail, Message
# from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
# CORS(app)

from . import weather, errors, default, auth

if __name__ == "__main__":
    app.run(debug=int(getenv("DEBUG")), port=int(getenv("PORT")))