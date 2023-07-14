from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/dojo')
def repeat_dojo():
    return "dojo!"

@app.route('/say/<username>')
def repeat_name(username):
    return f"Hi {username}"

@app.route('/say/<int:number>/<username>')
def repeat_number_name(username,number):
    tmp = []
    for i in range(int(number)+1):
        tmp[i] = f"Hi {username}"
    return tmp

if __name__ == '__main__':
    app.run(debug=True)