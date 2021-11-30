from application import db

class Young_Mind(db.Model):
  	id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(Text(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
	jokes = db.relationship(Young_Mind, backref'young_mind')
 
class Jokes(db.Model):
    id = Column(db.Integer, primary_key=True)
    joke_Category= db.relationship('Category')
    young_mind_id = db.Column(db.Integer, ForeignKey('young_Mind.id'), nullable=False)