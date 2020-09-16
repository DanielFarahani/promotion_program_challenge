from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL

class PromotionForm(Form):
    firstname = StringField(
        'name', validators=[DataRequired()]
    )
    lastname = StringField(
        'city', validators=[DataRequired()]
    )    
    #TODO add email validator
    email = StringField(
        'email', validators=[DataRequired()]
    )
    code = StringField(
        'code_value', validators=[URL()]
    )
