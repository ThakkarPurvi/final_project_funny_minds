from application import db

class YoungMind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    jokes = db.relationship("Joke", backref="youngmind")

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke_category = db.Column(db.String(50), nullable=False)
    joke_description = db.Column(db.String(500), nullable=False)

    youngmind_id = db.Column(db.Integer, db.ForeignKey("young_mind.id"), nullable=False)