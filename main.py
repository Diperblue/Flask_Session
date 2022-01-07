from flask import Flask, session

app = Flask(__name__)

@app.route('/')
def initial() -> 'html':
    return 'Testando'

app.run(debug=True)
