from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Form, IntegerField, SelectField, TextAreaField, HiddenField, RadioField, FileField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    name = StringField(label='Nombre', validators=[DataRequired()])
    email = EmailField(label='Correo', validators=[DataRequired(), Email()])
    company = StringField(label='Empresa')
    phone = StringField(label='Telefono')
    message = StringField(label='Mensaje', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField(label='ENVIAR')


class RegisterForm(FlaskForm):
    org_number = StringField(label='Número VAT (CIF)', validators=[DataRequired()])
    company_name = StringField(label='Nombre de Empresa', validators=[DataRequired()])
    contact_name = StringField(label='Nombre de Persona', validators=[DataRequired()])
    email = EmailField(label='Correo', validators=[DataRequired(), Email()])
    phone = StringField(label='Telefono', validators=[DataRequired()])
    type_company = StringField(label='Typo de Actividad de la empresa')
    address = StringField(label='Dirección (donde recogimos coladas)', validators=[DataRequired()])
    submit = SubmitField(label='RegistrarMe')