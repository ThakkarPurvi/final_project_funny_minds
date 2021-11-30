from application import db

class Young_Mind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    jokes = db.relationship("Jokes", backref="Young_Mind")

class Jokes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke_category = db.Column(db.String(50), nullable=False)
    joke_description = db.Column(db.String(500), nullable=False)
    young_mind_id = db.Column(db.Integer, db.ForeignKey("young_mind.id"), nullable=False)