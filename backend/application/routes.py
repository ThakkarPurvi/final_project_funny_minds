from application import app, db
from application.models import Young_Mind, Jokes
from flask import request, Response, jsonify
from os import getenv

#Create Young Minds
@app.route('/create/Young_Mind', methods=["POST"])
def create_Young_Mind():
    json = request.json
    new_Young_Mind = Young_Mind(
        name = json["name"],
        country = json["country"],
        dob = json["dob"]
    )
    db.session.add(new_Young_Mind)
    db.session.commit()
    return f"Young_Mind '{new_Young_Mind.name}' added to database"

#Create Joke
@app.route('/create/joke/<int:planet_id>', methods=["POST"])
def create_joke(young_mind_id):
    json = request.json
    new_joke = Joke(
        joke_category = json["joke_category"],
        young_mind_id = young_mind_id,
        joke_description = json["joke_description"]
    )
    db.session.add(new_joke)
    db.session.commit()
    return f"Joke '{new_joke.name}' added to database"

#Get all Young Minds
@app.route('/get/allYoung_Mind', methods=["GET"])
def get_all_Young_Mind():
    all_Young_Mind = Young_Mind.query.all()
    json = {"Young_Minds": []}
    for Young_Mind in all_Young_Minds:
        jokes = []
        for joke in Young_Mind.jokes:
            jokes.append(
                {
                    "id": joke.id,
                    "joke_category": joke.joke_category,
                    "young_mind_id": joke.young_mind_id,
                    "joke_description": joke.joke_description
                }
            )
        json["Young_Minds"].append(
            {
                "id": Young_Mind.id,
                "name": Young_Mind.name,
                "country": Young_Mind.country,
                "dob": Young_Mind.dob,
                "jokes": jokes
            }
        )
    return jsonify(json)

@app.route('/get/allJokes', methods=["GET"])
def get_all_jokes():
    all_jokes = Young_Mind.query.all()
    json = {"jokes": []}
    for joke in all_jokes:
        json["jokes"].append(
            {
                "id": joke.id,
                "joke_category": joke.joke_category,
                "young_mind_id": joke.young_mind_id,
                "joke_description": joke.joke_description
            }
        )
    return jsonify(json)

@app.route('/get/Young_Mind/<int:id>', methods=["GET"])
def get_Young_Mind(id):
    Young_Mind = Young_Mind.query.get(id)
    return jsonify(
        {
            "id": Young_Mind.id,
            "name": Young_Mind.name,
            "country": Young_Mind.country,
            "dob": Young_Mind.dob
        }
    )

@app.route('/get/Young_Mind/<int:id>/jokes', methods=["GET"])
def get_jokes(id):
    jokes = Young_Mind.query.get(id).jokes
    json = {"jokes": []}
    for joke in jokes:
        json["jokes"].append(
            {
                "id": joke.id,
                "joke_category": joke.joke_category,
                "young_mind_id": joke.young_mind_id,
                "joke_description": joke.joke_description
            }
        )
    return jsonify(json)

@app.route('/update/young_mind/<int:id>', methods=["PUT"])
def update_young_mind(id):
    data = request.json
    young_mind = young_mind.query.get(id)
    Young_Mind.name = data["name"]
    Young_Mind.country = data["country"]
    Young_Mind.dob = data["dob"]
    db.session.commit()
    return f"Young_Mind '{Young_Mind.name}' updated successfully"

@app.route('/delete/Young_Mind/<int:id>', methods=["DELETE"])
def delete_Young_Mind(id):
    Young_Mind = Young_Mind.query.get(id)
    db.session.delete(Young_Mind)
    return f"Young_Mind '{Young_Mind.name}' deleted successfully"