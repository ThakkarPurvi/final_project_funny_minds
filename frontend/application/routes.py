from application import app
from application.forms import CreateYoung_MindForm, CreateJokeForm
from flask import render_template, request, redirect, url_for, jsonify
import requests
from os import getenv

backend = getenv("BACKEND_HOSTNAME")

# Read Young_Mind
@app.route('/', methods=["GET"])
def home():
    all_Young_Mind = requests.get(f"http://{backend}/ret/allYoung_Minds").json()["Young_Mind"]
    return render_template('index.html', title="Home", Young_Minds=Young_Minds)

# Create Jokes
@app.route('/create/Young_Mind', methods=["GET","POST"])
def create_Young_Mind():
    form = CreateYoung_MindForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend}/create/Young_Mind",
            json={
                "name": form.name.data,
                "country": form.country.data,
                "dob": form.dob.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_Young_Mind.html", title="Add a new Young_Mind", form=form)

@app.route('/create/joke', methods=["GET","POST"])
def create_joke():
    form = CreateYoung_MindForm()

    json = requests.get(f"http://{backend}/get/allYoung_Minds").json()
    for Young_Mind in json["Young_Minds"]:
        form.Young_Mind.choices.append((Young_Mind["id"], Young_Mind["name"], Young_Mind["country"], Young_Mind["dob"]))

    if request.method == "POST":
        response = requests.post(
            f"http://{backend}/create/joke/{form.Young_Mind.data}",
            json={
                "joke_category": form.joke_category.data,
                "young_mind_id": form.young_mind_id.data,
                "joke_description": form.joke_description.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_joke.html", title="Add Joke", form=form)

# Update Jokes
# # @app.route('/update/joke/<int:id>', methods=['GET','POST'])
# # def update_joke(id):
#     form = TaskForm()
#     joke = requests.get(f"http://{backend_host}/read/joke/{id}").json()
#     app.logger.info(f"joke: {joke}")

#     if request.method == "POST":
#         response = requests.put(
#         f"http://{backend_host}/update/joke/{id}",
#         json={"description": form.description.data}
#         )
#         return redirect(url_for('home'))

#     return render_template('update_joke.html', joke=joke, form=form)

# # Delete Jokes
# @app.route('/delete/joke/<int:id>')
# def delete_joke(id):
#     response = requests.delete(
#         f"http://{backend_host}/delete/joke/{id}"
#         )
#     return redirect(url_for('home'))

# # Read Jokes # Read Jokes # Read Jokes # Read Jokes # Read Jokes
# @app.route('/')
# @app.route('/home')
# def home():
#     all_jokes = requests.get(f"http://{backend_host}/read/alljokes").json()
#     app.logger.info(f"jokes: {all_jokes}")
#     return render_template('index.html', title="Home", all_jokes=all_jokes["jokes"])

# # Create Jokes
# @app.route('/create/joke', methods=['GET','POST'])
# def create_joke():
#     form = TaskForm()

#     if request.method == "POST":
#         response = requests.post(
#             f"http://{backend_host}/create/joke",
#             json={"description": form.description.data}
#         )
#         app.logger.info(f"Response: {response.text}")
#         return redirect(url_for('home'))

#     return render_template("create_joke.html", title="Share a new joke", form=form)

# # Update Jokes
# @app.route('/update/joke/<int:id>', methods=['GET','POST'])
# def update_joke(id):
#     form = TaskForm()
#     joke = requests.get(f"http://{backend_host}/read/joke/{id}").json()
#     app.logger.info(f"joke: {joke}")

#     if request.method == "POST":
#         response = requests.put(
#         f"http://{backend_host}/update/joke/{id}",
#         json={"description": form.description.data}
#         )
#         return redirect(url_for('home'))

#     return render_template('update_joke.html', joke=joke, form=form)

# # Delete Jokes
# @app.route('/delete/joke/<int:id>')
# def delete_joke(id):
#     response = requests.delete(
#         f"http://{backend_host}/delete/joke/{id}"
#         )
#     return redirect(url_for('home'))

# # Complete Jokes
# @app.route('/complete/joke/<int:id>')
# def complete_joke(id):
#     response = requests.put(
#         f"http://{backend_host}/complete/joke/{id}"
#         )
#     return redirect(url_for('home'))

# # InComplete Jokes
# @app.route('/incomplete/joke/<int:id>')
# def incomplete_joke(id):
#     response = requests.put(
#     f"http://{backend_host}/incomplete/joke/{id}"
#     )
#     return redirect(url_for('home'))