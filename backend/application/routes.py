from application import app, db
from application.models import YoungMind, Joke
from flask import request, Response, jsonify
from os import getenv

#Create Young Minds
@app.route('/create/YoungMind', methods=["POST"])
def create_YoungMind():
    json = request.json
    new_YoungMind = YoungMind(
        name = json["name"],
        country = json["country"],
        dob = json["dob"]
    )
    db.session.add(new_YoungMind)
    db.session.commit()
    return f"YoungMind '{new_YoungMind.name}' added to database"

#Create Joke
@app.route('/create/joke/<int:youngmind_id>', methods=["POST"])
def create_joke(youngmind_id):
    json = request.json
    new_joke = Joke(
        joke_category = json["joke_category"],
        youngmind_id = youngmind_id,
        joke_description = json["joke_description"]
    )
    db.session.add(new_joke)
    db.session.commit()
    return f"Joke '{new_joke.name}' added to database"

#Get all Young Minds
@app.route('/read/allYoungMind', methods=["GET"])
def get_all_YoungMind():
    all_YoungMind = YoungMind.query.all()
    json = {"YoungMind": []}
    for youngmind in all_YoungMind:
        jokes = []
        for joke in youngmind.jokes:
            jokes.append(
                {
                    "id": joke.id,
                    "joke_category": joke.joke_category,
                    "youngmind_id": joke.youngmind_id,
                    "joke_description": joke.joke_description
                }
            )
        json["YoungMind"].append(
            {
                "id": youngmind.id,
                "name": youngmind.name,
                "country": youngmind.country,
                "dob": youngmind.dob,
                "jokes": jokes
            }
        )
    return jsonify(json)

@app.route('/get/allJokes', methods=["GET"])
def get_all_jokes():
    all_jokes = YoungMind.query.all()
    json = {"jokes": []}
    for joke in all_jokes:
        json["jokes"].append(
            {
                "id": joke.id,
                "joke_category": joke.joke_category,
                "youngmind_id": joke.youngmind_id,
                "joke_description": joke.joke_description
            }
        )
    return jsonify(json)

@app.route('/get/YoungMind/<int:id>', methods=["GET"])
def get_YoungMind(id):
    youngmind = YoungMind.query.get(id)
    return jsonify(
        {
            "id": youngmind.id,
            "name": youngmind.name,
            "country": youngmind.country,
            "dob": youngmind.dob
        }
    )

@app.route('/get/YoungMind/<int:id>/jokes', methods=["GET"])
def get_jokes(id):
    jokes = YoungMind.query.get(id).jokes
    json = {"jokes": []}
    for joke in jokes:
        json["jokes"].append(
            {
                "id": joke.id,
                "joke_category": joke.joke_category,
                "youngmind_id": joke.youngmind_id,
                "joke_description": joke.joke_description
            }
        )
    return jsonify(json)

@app.route('/update/youngmind/<int:id>', methods=["PUT"])
def update_youngmind(id):
    data = request.json
    youngmind = YoungMind.query.get(id)
    youngmind.name = data["name"]
    youngmind.country = data["country"]
    youngmind.dob = data["dob"]
    db.session.commit()
    return f"YoungMind '{youngmind.name}' updated successfully"

@app.route('/delete/YoungMind/<int:id>', methods=["DELETE"])
def delete_YoungMind(id):
    youngmind = YoungMind.query.get(id)
    db.session.delete(youngmind)
    return f"YoungMind '{youngmind.name}' deleted successfully"