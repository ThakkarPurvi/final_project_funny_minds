from application import app
from application.forms import CreateYoungMindForm, CreateJokeForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "final_project_young_minds_backend:5000"

# Read YoungMind
@app.route('/', methods=["GET"])
def home():
    all_youngmind = requests.get(f"http://{backend_host}/read/allYoungMind").json()["YoungMind"]
    return render_template('index.html', title="Home", all_youngmind=all_youngmind)

# Create Jokes
@app.route('/create/YoungMind', methods=["GET","POST"])
def create_YoungMind():
    form = CreateYoungMindForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/YoungMind",
            json={
                "name": form.name.data,
                "country": form.country.data,
                "dob": form.dob.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_YoungMind.html", title="Add a new YoungMind", form=form)

@app.route('/create/joke', methods=["GET","POST"])
def create_joke():
    form = CreateYoungMindForm()

    json = requests.get(f"http://{backend_host}/get/allYoungMind").json()
    for youngmind in json["youngminds"]:
        form.youngmind.choices.append((youngmind["id"], youngmind["name"]))

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/joke/{form.youngmind.data}",
            json={
                "joke_category": form.joke_category.data,
                "youngmind_id": form.youngmind_id.data,
                "joke_description": form.joke_description.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_joke.html", title="Add Joke", form=form)