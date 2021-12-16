from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class TodoForm(FlaskForm):
    title = StringField(label='Task Title', validators=[DataRequired()])
    end_date = DateField(label='Completion Date', validators=[DataRequired()])
    submit_form = SubmitField(label='Add Todo')
