from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/lyb/')
def lyb():
    return render_template('lyb.html')
if __name__=="__main__":
    app.run(host='0.0.0.0',port='444')
