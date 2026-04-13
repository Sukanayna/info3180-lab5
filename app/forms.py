# Add any form classes for Flask-WTF 
from forms import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Regexp
from flask_wtf.file import FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Movie Description', validators=[DataRequired(), Length(max=500)])
    poster = FileField('Movie Poster', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
