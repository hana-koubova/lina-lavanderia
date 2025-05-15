from flask import Flask, render_template, request, url_for, redirect, flash, session, jsonify, send_file, send_from_directory, make_response
from flask_bootstrap import Bootstrap5
import os
from forms import ContactForm, RegisterForm
from flask_mail import Mail, Message
from werkzeug.exceptions import HTTPException


## WTFORMS

from flask_wtf.csrf import CSRFProtect

## Inner Dependencies

from database import db, pre_approve, user_companies

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

bootstrap = Bootstrap5(app)

## CSFP protection

csrf = CSRFProtect(app)
csrf.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'koubovahan@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'lina@contact.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContactForm()
    negocios = [
        'Spa y Masajes',
        'Restaurantes',
        'Clubes Deportivos',
        'Hoteles y Apartamentos',
        'Estéticas',
        'y Más'
    ]

    if form.validate_on_submit() and request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        company = request.form['company']
        phone = request.form['phone']
        message = request.form['message']
        print('Form accepted')

        msg = Message( 
                subject='Contact Form',  
                recipients = ['koubovahan@gmail.com'] 
               ) 
        #msg.subject = {email}
        msg.body = f"Name: {name}\nEmail: {email}\nCompany: {company}\nPhone: {phone}\nMessage: {message}"
        print('Msg created')
        mail.send(msg)

    return render_template('index.html',
                           negocios=negocios,
                           form=form)


@app.route('/inscribirse', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    message = None
    if form.validate_on_submit() and request.method == 'POST':
        #nunmber_to_check = request.form['org_number']
        duplicate = list(user_companies.find({'org_number': request.form['org_number']}))
        if len(duplicate) > 0:
            message = 'Ya hay empresa con este número en nuestra base de datos.'
            return render_template('register.html',
                    form = form,
                    message = message)
        
        new_register = {
            'org_number': request.form['org_number'],
            'company_name': request.form['company_name'],
            'contact_name': request.form['contact_name'], 
            'email': request.form['email'],
            'phone': request.form['phone'],
            'type_company': request.form['type_company'],
            'address': request.form['address'],
            'approved': False
            }
        user_companies.insert_one(new_register)
        msg = Message( 
                subject='Lina - New Register',  
                recipients = ['koubovahan@gmail.com'] 
               )
        msg.body = 'Hi, there is a new register in your system. You are allowed to buy one t-shirt :)'
        mail.send(msg)
        return redirect(url_for('register_success'))
    return render_template('register.html',
                    form = form,
                    message = message)

@app.route('/insription-completo')
def register_success():
    return render_template('register_success.html')

@app.route('/como_funcciona')
def como_funcciona():
    return render_template('como_funcciona.html')

@app.route("/test", methods=['GET', 'POST'])
def test():
    msg = Message( 
                subject='Test', 
                recipients = ['koubovahan@gmail.com'] 
               )
    try:
        mail.send(msg)
        return 'Email sent'
    except HTTPException as error:

        return error



if __name__ == "__main__":
    app.run(debug=True)