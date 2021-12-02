from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class CreateYoung_MindForm(FlaskForm):
    name = StringField('Young_Mind Name', validators=[DataRequired()])
    country = IntegerField('Young_Mind country', validators=[DataRequired()])
    dob = SelectField('Young_Mind dob', validators=[DataRequired()]
    submit = SubmitField('Add Young_Mind')

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
    Young_Mind = SelectField('Creating Young_Mind', validators=[DataRequired()], choices=[])
    submit = SubmitField('Add Joke')