from .. import app



@app.get("/")
def index():
    return "index"

@app.get("/about")
def about():
    return "about"