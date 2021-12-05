from application import app, db
from application.models import YoungMind, Joke
from flask import request, Response, jsonify, render_template, redirect, url_for
import os

#Create Young Minds
@app.route('/create/youngmind', methods=["POST"])
def create_youngmind():
    json = request.json
    new_youngmind = YoungMind(
        name = json["name"]
    )
    db.session.add(new_youngmind)
    db.session.commit()
    return f"YoungMind '{new_youngmind.name}' added to database"

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
@app.route('/get/allYoungMinds', methods=["GET"])
def get_all_YoungMinds():
    all_youngminds = YoungMind.query.all()
    json = {"youngminds": []}
    for youngmind in all_youngminds:
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
        json["youngminds"].append(
            {
                "id": youngmind.id,
                "name": youngmind.name,
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
def get_youngmind(id):
    youngmind = YoungMind.query.get(id)
    return jsonify(
        {
            "id": youngmind.id,
            "name": youngmind.name
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

#Update youngmind
@app.route('/update/youngmind/<int:id>', methods=["PUT"])
def update_youngmind(id):
    data = request.json
    youngmind = YoungMind.query.get(id)
    youngmind.name = data["name"]
    db.session.commit()
    return f"YoungMind '{youngmind.name}' updated successfully"

#Delete youngmind
@app.route('/delete/youngmind/<int:id>', methods=["DELETE"])
def delete_youngmind(id):
    youngmind = YoungMind.query.get(id)
    db.session.delete(youngmind)
    db.session.commit()
    return f"YoungMind '{youngmind.name}' deleted successfully"

#Update joke
@app.route('/update/joke/<int:id>', methods=["PUT"])
def update_joke(id):
    data = request.json
    joke = Joke.query.get(id)
    joke.joke_description = data["joke_description"],
    joke.joke_category = data["joke_category"]
    db.session.commit()
    return f"Joke '{joke.name}'updated successfully"

#Delete Joke
@app.route('/delete/joke/<int:id>', methods=["DELETE"])
def delete_joke(id):
    joke = Joke.query.get(id)
    db.session.delete(joke)
    db.session.commit()
    return f"Joke '{joke.name}' deleted successfully"
