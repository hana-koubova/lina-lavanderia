from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Form, IntegerField, SelectField, TextAreaField, HiddenField, RadioField, FileField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    name = StringField(label='Nombre', validators=[DataRequired()])
    email = EmailField(label='Correo', validators=[DataRequired(), Email()])
    company = StringField(label='Empresa')
    phone = StringField(label='Telefono')
    message = StringField(label='Mensaje', widget=TextArea())
    submit = SubmitField(label='ENVIAR')