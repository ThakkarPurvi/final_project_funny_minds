from wtforms import StringField, IntegerField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class CreateYoungMindForm(FlaskForm):
    name = StringField('YoungMind Name', validators=[DataRequired()])
    country = IntegerField('YoungMind country', validators=[DataRequired()])
    dob = DateField('YoungMind dob', validators=[DataRequired()])
    submit = SubmitField('Add YoungMind')

class CreateJokeForm(FlaskForm):
    joke_category = StringField('Joke joke_category', validators=[DataRequired()],
        choices=[
            ("Knock-Knock", "Knock-Knock"),
            ("Summer Jokes", "Summer Jokes"),
            ("Sports Jokes", "Sports Jokes"),
            ("Festive Jokes", "Festive Jokes"),
            ("Birthday Jokes", "Birthday Jokes"),
            ("Santa Jokes", "Santa Jokes"),
            ("Others", "Others")
        ]
    )
    joke_description = IntegerField('Joke joke_description', validators=[DataRequired()])
    youngmind = SelectField('Creating YoungMind', validators=[DataRequired()], choices=[])
    submit = SubmitField('Add Joke')