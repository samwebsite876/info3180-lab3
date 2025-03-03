from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name (Required)', validators=[DataRequired()])
    email = StringField('Email (Required)', validators=[DataRequired(), Email()])
    subject = StringField('Subject (Required)', validators=[DataRequired()])
    message = TextAreaField('Message (Required)', validators=[DataRequired()])
    submit = SubmitField('Send')