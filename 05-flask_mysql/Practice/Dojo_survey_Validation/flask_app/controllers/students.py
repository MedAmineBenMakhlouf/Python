from flask import  render_template, redirect, request
from flask_app import app
from flask_app.models.student import Student
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/')
def dashboard():
    # all_dojos = Dojo.get_all()
    return render_template('index.html')



@app.route('/students/create', methods=['POST'])
def create():
    if Student.validation(request.form):
        id = Student.create(request.form)
        student = Student.get_student_by_id({'id':id})
        return render_template('result.html',student=student)
    return redirect('/')