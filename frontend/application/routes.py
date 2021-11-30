from application import app
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "young_minds_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_jokes = requests.get(f"http://{backend_host}/read/alljokes").json()
    app.logger.info(f"jokes: {all_jokes}")
    return render_template('index.html', title="Home", all_jokes=all_jokes["jokes"])

@app.route('/create/joke', methods=['GET','POST'])
def create_joke():
    form = TaskForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/joke",
            json={"description": form.description.data}
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_joke.html", title="Share a new joke", form=form)

@app.route('/update/joke/<int:id>', methods=['GET','POST'])
def update_joke(id):
    form = TaskForm()
    joke = requests.get(f"http://{backend_host}/read/joke/{id}").json()
    app.logger.info(f"joke: {joke}")

    if request.method == "POST":
        response = requests.put(
        f"http://{backend_host}/update/joke/{id}",
        json={"description": form.description.data}
        )
        return redirect(url_for('home'))

    return render_template('update_joke.html', joke=joke, form=form)

@app.route('/delete/joke/<int:id>')
def delete_joke(id):
    response = requests.delete(
        f"http://{backend_host}/delete/joke/{id}"
        )
    return redirect(url_for('home'))

@app.route('/complete/joke/<int:id>')
def complete_joke(id):
    response = requests.put(
        f"http://{backend_host}/complete/joke/{id}"
        )
    return redirect(url_for('home'))

@app.route('/incomplete/joke/<int:id>')
def incomplete_joke(id):
    response = requests.put(
    f"http://{backend_host}/incomplete/joke/{id}"
    )
    return redirect(url_for('home'))