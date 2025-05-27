from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Form, IntegerField, SelectField, TextAreaField, HiddenField, RadioField, FileField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditor, CKEditorField

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
    terms_accept = BooleanField(u"He leído y acepto los Términos y Condiciones del servicio.", validators=[DataRequired()])
    submit = SubmitField(label='RegistrarMe')

class AdminForm(FlaskForm):
    #email = StringField(label='Email', validators=[DataRequired(), Email(message="Email format not valid")])
    admin_name = StringField(label='Admin Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Access Admin Area")

class LegalForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    text = CKEditorField(label="Job Description", validators=[DataRequired()])
    submit = SubmitField(label='Save text')