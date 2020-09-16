from flask_wtf import Form
from wtforms.fields.html5 import EmailField 
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Email, Length

class PromotionForm(Form):
    firstname = StringField(
        'name', validators=[DataRequired()]
    )
    lastname = StringField(
        'city', 
        validators=[DataRequired()]
    )    
    email = EmailField(
        'email', 
        validators=[DataRequired(), Email()]
    )
    code = TextField(
        'code_value', validators=[DataRequired(), 
            Length(min=8, max=8, message=('Enter a valid code'))]
    )
