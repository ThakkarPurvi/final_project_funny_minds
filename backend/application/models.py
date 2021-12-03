from application import db

class YoungMind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    
    jokes = db.relationship("Joke", backref="youngmind")

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke_category = db.Column(db.String(50), nullable=False)
    joke_description = db.Column(db.String(500), nullable=False)
    YoungMind_id = db.Column(db.Integer, db.ForeignKey("young_mind.id"), nullable=False)