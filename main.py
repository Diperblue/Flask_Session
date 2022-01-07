from flask import Flask, render_template, session, escape, request
from user import user

app = Flask(__name__, template_folder='template')

app.secret_key = 'Biscoito'

@app.route('/')
def index() -> 'html':
    return render_template('index.html')

@app.route('/setuser', methods=['POST'])
def cruser() -> 'html':
    name = request.form['name']
    return 'O usuario', name

app.run(debug=True)
