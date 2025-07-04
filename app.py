from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('trial.html')

@app.route('/fix')
def fix():
    return render_template('fix.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)