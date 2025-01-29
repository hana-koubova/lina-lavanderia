from flask import Flask, render_template, request, url_for, redirect, flash, session, jsonify, send_file, send_from_directory, make_response
from flask_bootstrap import Bootstrap5
import os
from forms import ContactForm
from flask_mail import Mail, Message


## WTFORMS

from flask_wtf.csrf import CSRFProtect

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
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContactForm()
    negocios = [
        'Spa y Masasjes',
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
        flash('Mensaje se ha envidado! Te contactaremos pronto.')


        msg = Message( 
                message, 
                sender = 'koubovahan@gmail.com', 
                recipients = ['koubovahan@gmail.com'] 
               ) 
        msg.subject = {email}
        #msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        mail.send(msg) 

        return 'Mail has sent dude!'

    return render_template('index.html',
                           negocios=negocios,
                           form=form)



if __name__ == "__main__":
    app.run(debug=True)