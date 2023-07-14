from flask import Flask, render_template

app = Flask(__name__)

#http://127.0.0.1:5000
# http://localhost:5000

@app.route('/')
def index():
    return "hello from flask"

@app.route('/hi')
def index_1():
    return "<h1>Hi every one</h1>"

@app.route('/hi/<username>/<int:age>')
def hi_user(username,age):
    return f"<h1>Hi {username} your age : {age}</h1>"

@app.route('/template')
def circle():
    return render_template("index.html")

@app.route('/template/<url_color>/<int:number>')
def circles(url_color,number):
    print("*"*20, url_color, "*"*20)
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("index.html", color=url_color, number=number,students=student_info)

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5003)