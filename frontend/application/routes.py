from application import app
from application.forms import CreateYoungMindForm, CreateJokeForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "final_project_young_minds_backend:5000"

# Get YoungMind
@app.route('/', methods=["GET"])
def home():
    youngminds = requests.get(f"http://{backend_host}/get/allYoungMinds").json()["youngminds"]
    return render_template('index.html', title="Home", youngminds=youngminds)

# Create YoungMind
@app.route('/create/youngmind', methods=["GET","POST"])
def create_youngmind():
    form = CreateYoungMindForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/youngmind",
            json={
                "name": form.name.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_YoungMind.html", title="Add a new YoungMind", form=form)

#Create Joke
@app.route('/create/joke', methods=["GET","POST"])
def create_joke():
    form = CreateJokeForm()

    json = requests.get(f"http://{backend_host}/get/allYoungMinds").json()
    for youngmind in json["youngminds"]:
        form.youngmind.choices.append((youngmind["id"], youngmind["name"]))

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/joke/{form.youngmind.data}",
            json={
                "joke_category": form.joke_category.data,
                "joke_description": form.joke_description.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_Joke.html", title="Add Joke", form=form)

# Update youngmind
@app.route('/update/youngmind/<int:id>', methods=["GET","POST"])
def update_youngmind(id):
    form = CreateYoungMindForm()
    youngmind = requests.get(f"http://{backend_host}/get/YoungMind/{id}").json()

    if request.method == "POST":
        response = requests.put(
            f"http://{backend_host}/update/youngmind/{id}",
            json={
                "name": form.name.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("update_YoungMind.html", youngmind=youngmind, title="Updated Successfully", form=form)

#Delete youngmind
@app.route('/delete/youngmind/<int:id>')
def delete_youngmind(id):
    response = requests.delete(f"http://{backend_host}/delete/youngmind/{id}")
    return redirect(url_for('home'))

#Update joke
@app.route('/update/joke/<int:id>', methods = ['GET', 'POST'])
def update_joke(id):
    form = CreateJokeForm()
    joke = requests.get(f"http://{backend_host}/read/joke/{id}").json()
    if request.method == "POST":
        response = requests.put(f"http://{backend_host}/update/joke/{id}", json={"joke_description": form.joke_description.data, "joke_category": form.joke_category.data } )
        return redirect(url_for('home'))

    return render_template("update_Joke.html", joke=joke, form=form, title = "Update")

#Delete joke
@app.route('/delete/joke/<int:id>')
def delete_joke(id):
    response = requests.delete(f"http://{backend_host}/delete/joke/{id}")
    return redirect(url_for('home'))