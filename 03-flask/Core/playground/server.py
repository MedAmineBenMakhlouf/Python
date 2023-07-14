from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def index(number=3):
    return render_template("index.html", number=number)

@app.route('/play/<int:number>')
def with_number(number):
    return render_template("index.html", number=number)

@app.route('/play/<int:number>/<color_name>')
def color_with_number(number,color_name):
    return render_template("index.html", number=number, color_name=color_name)

if __name__ == '__main__':
    app.run(port=5004, debug=True)