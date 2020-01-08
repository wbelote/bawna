from app import app


@app.route("/")
def home():
    return "<h2>Coming Soon</h2>"
