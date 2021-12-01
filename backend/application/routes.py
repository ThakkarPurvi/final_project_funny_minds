from application import app, db
from application.models import Jokes, Young_Mind
from flask import render_template, request, redirect, url_for, Response, jsonify

#Create Young Minds
@app.route('/create/Young_Mind', methods=['GET','POST'])
def create_Young_Mind():
        package = request.json
        new_Young_Mind = Young_Mind(name=package["name"], country=package["country"], dob=package["dob"])
        db.session.add(new_Young_Mind)
        db.session.commit()
        return Response(f"Added Young_Mind: {new_Young_Mind.name}to{new_Young_Mind.country}born on{new_Young_Mind.dob}", mimetype='text/plain')

#Read Young Minds
@app.route('/read/Young_Mind', methods=['GET'])
def read_Young_Mind():
    all_Young_Mind = Young_Mind.query.all()
    Young_Mind_dict = {"Young_Minds": []}
    for Young_Mind in all_Young_Mind:
        Young_Mind_dict["Young_Mind"].append(
            {
                "id": Young_Mind.id, 
                "description": Young_Mind.description,
                "completed": Young_Mind.completed
            }
        )
    return jsonify(Young_Mind_dict)

# #Update Young Minds
# @app.route('/update/Young_Mind/<int:id>', methods=['PUT'])
# def update_Young_Mind(id):
#     package = request.json
#     Young_Mind = Young_Mind.query.get(id)
#     Young_Mind.description = package["description"]
#     db.session.commit()
#     return Response(f"Updated Young_Mind (ID: {id}) with description: {Young_Mind.description}", mimetype='text/plain')

# #Delete Young Minds
# @app.route('/delete/Young_Mind/<int:id>', methods=['DELETE'])
# def delete_Young_Mind(id):
#     Young_Mind = Young_Mind.query.get(id)
#     db.session.delete(Young_Mind)
#     db.session.commit()
#     return Response(f"Delete Young_Mind ID: {id}" , mimetype='text/plain')

# #Create Joke
# @app.route('/create/joke', methods=['GET','POST'])
# def create_joke():
#         package = request.json
#         new_joke = jokes(description=package["description"])
#         db.session.add(new_joke)
#         db.session.commit()
#         return Response(f"Added joke with description: {new_joke.description}", mimetype='text/plain')

# #Read Joke
# @app.route('/read/alljokes', methods=['GET'])
# def read_jokes():
#     all_jokes = jokes.query.all()
#     jokes_dict = {"jokes": []}
#     for joke in all_jokes:
#         jokes_dict["jokes"].append( 
#             {
#                 "id": joke.id,
#                 "description": joke.description,
#                 "completed": joke.completed
#             }
#         )
#     return jsonify(jokes_dict)

# #Update Joke
# @app.route('/update/joke/<int:id>', methods=['PUT'])
# def update_joke(id):
#     package = request.json
#     joke = jokes.query.get(id)
#     joke.description = package["description"]
#     db.session.commit()
#     return Response(f"Updated joke (ID: {id}) with description: {joke.description}", mimetype='text/plain')

# #Delete Joke
# @app.route('/delete/joke/<int:id>', methods=['DELETE'])
# def delete_joke(id):
#     joke = jokes.query.get(id)
#     db.session.delete(joke)
#     db.session.commit()
#     return Response(f"Delete joke ID: {id}" , mimetype='text/plain')

# #Complete Joke
# @app.route('/complete/joke/<int:id>', methods=['PUT'])
# def complete_joke(id):
#     joke = jokes.query.get(id)
#     joke.completed = True
#     db.session.commit()
#     return Response(f"joke with ID: {id} set to completed = True", mimetype='text/plain')

# #InComplete Joke
# @app.route('/incomplete/joke/<int:id>', methods=['PUT'])
# def incomplete_joke(id):
#     joke = jokes.query.get(id)
#     joke.completed = False
#     db.session.commit()
#     return Response(f"joke with ID: {id} set to completed = False", mimetype='text/plain')