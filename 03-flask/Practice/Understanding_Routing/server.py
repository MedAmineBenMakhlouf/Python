from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/dojo')
def repeat_dojo():
    return "dojo!"

@app.route('/say/<string:username>')
def repeat_name(username):
    if str(username):
        return f"Hi {username}"
    return f"{username} should be a string"

@app.route('/say/<int:number>/<string:username>')
def repeat_number_name(username,number):
    response=""
    for i in range(number):
        response += f"<h3> {username} </h3>"
    return response
    # return render_template("index.html",number=number, username=username)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def handle_undefined_routes(path):
    return "Sorry! No response. Try again."

if __name__ == '__main__':
    app.run(debug=True )