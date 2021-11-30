from application import app
from application import routes

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')




from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "Young Minds Website"
    return render_template("index.html", title=title)

@app.route('/login')
def login():
    title = "Login to share your joke and riddles"
    return render_template("login.html", title=title)
