from flask import  render_template, redirect, request,session
from flask_app import app
from flask_app.models.email import Email
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/')
def emails():    
    
    return render_template('index.html')

@app.route('/success')
def success():
    emails = Email.get_all()
    last_email = Email.get_by_id({'id': session['id']})
    return render_template('view.html',all_mails=emails, last_one=last_email)

@app.route('/emails/create', methods=['POST'])
def create():
    if Email.validate_email(request.form):
        email_id = Email.create(request.form)
        session['id'] = email_id
        return redirect('/success')
    return redirect('/')

@app.route('/email/<int:email_id>/delete')
def delete(email_id):
    Email.delete_email({'id':email_id})
    return redirect('/success')