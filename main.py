from flask import Flask, render_template, request, url_for, redirect, flash, session, jsonify, send_file, send_from_directory, make_response
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    negocios = [
        'Spa y Masasjes',
        'Restaurantes',
        'Clubes Deportivos',
        'Hoteles y Apartamentos',
        'Estéticas',
        'y Más'
    ]
    return render_template('index.html',
                           negocios=negocios)



if __name__ == "__main__":
    app.run(debug=True)