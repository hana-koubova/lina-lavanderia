from flask import Flask, render_template, request, url_for, redirect, flash, session, jsonify, send_file, send_from_directory, make_response
from flask_bootstrap import Bootstrap5
import os
from forms import ContactForm
from flask_mail import Mail, Message
import mailtrap as mt


## WTFORMS

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

bootstrap = Bootstrap5(app)

## CSFP protection

csrf = CSRFProtect(app)
csrf.init_app(app)

#app.config['MAILTRAP_API_TOKEN'] = os.environ.get('MAILTRAP_API_TOKEN')

#def send_email_via_api(to_email, subject, body):
#    mail = mt.Mail(
#        sender=mt.Address(email="sender@example.com", name="Sender Name"),
#        to=[mt.Address(email=to_email)],
#        subject=subject,
#        text=body,
#    )
#    client = mt.MailtrapClient(token=os.environ.get('MAILTRAP_API_TOKEN'))
#    client.send(mail)
#    return True

## Mailtrap configuration for production

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

        ## FIRST OPTION
        # Compose email
        #msg = Message(subject='Contact Form Submission',
        #              sender=email,
        #              recipients=['koubovahan@gmail.com'],
        #              body=f"Name: {name}\nEmail: {email}\nMessage: {message}")
        
        # Send email
        #mail.send(msg)

        ## SECOND OPTION
        # Compose email

        msg = Message( 
                message, 
                sender = email, 
                recipients = 'koubovahan@gmail.com' 
               ) 
        msg.subject = 'Contact Form Submission'
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Send email via Mailtrap API
        #if send_email_via_api('koubovahan@gmail.com', subject, body):
        #    flash('Thank you for your message!')
        #else:
        #    flash('Failed to send message.')
        mail.send(msg) 

        return redirect(url_for('index'))

    return render_template('index.html',
                           negocios=negocios,
                           form=form)



if __name__ == "__main__":
    app.run(debug=True)