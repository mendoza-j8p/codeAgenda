from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/web/templates/home.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
