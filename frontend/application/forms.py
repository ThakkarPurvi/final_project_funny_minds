from wtforms import StringField, IntegerField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class CreateYoungMindForm(FlaskForm):
    name = StringField('Type your Name', validators=[DataRequired()])

    submit = SubmitField('Submit your name to share your Joke')

class CreateJokeForm(FlaskForm):
    joke_category = SelectField('Select Joke Category', validators=[DataRequired()],
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
    joke_description = StringField('Type your Joke', validators=[DataRequired()])
    youngmind = SelectField('Select your Name', validators=[DataRequired()], choices=[])
    
    submit = SubmitField('Submit Joke')