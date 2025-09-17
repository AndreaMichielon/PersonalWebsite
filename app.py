# app.py
from flask import Flask, send_file

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)