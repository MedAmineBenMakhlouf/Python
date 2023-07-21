from flask import Flask, render_template, request,redirect, session

app = Flask(__name__)

app.secret_key = "SEcretKey"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("PROCESS - FORM RECEIVED")
    print(f"first name {request.form['firstname']}\nlast name: {request.form['lastname']}\nage: {request.form['age']}")
    # never ever render on post request
    # return render_template("display.html", firstname=request.form['firstname'], lastname=request.form['lastname'], age=request.form['age'])
    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    session['age'] = request.form['age']
    return  redirect('/display')

@app.route('/display')
def display():
    # session['firstname']
    # print(session['lastname'])
    # print(session['age'])
    return render_template("display.html")

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/display')

if __name__ == '__main__':
    app.run(debug= True)