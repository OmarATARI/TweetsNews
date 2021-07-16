from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class ExportForm(FlaskForm):
  term = StringField('Recherche')
  author = StringField('Auteur')
  day_start = DateField('Date de début', format='%Y-%m-%d')
  hour_start = StringField('Heure de début', validators=[DataRequired()])
  day_end = DateField('Date de fin', format='%Y-%m-%d')
  hour_end = StringField('Heure de fin', validators=[DataRequired()])
  submit = SubmitField('Exporter')