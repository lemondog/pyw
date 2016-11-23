from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/lyb/')
def lyb():
    return render_template('lyb.html')
