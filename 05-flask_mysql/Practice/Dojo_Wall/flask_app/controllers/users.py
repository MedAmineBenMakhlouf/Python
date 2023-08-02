from flask import  render_template, redirect, request, flash,session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    messages = Message.get_all_user_messages({'id':session['user_id']})
    nbr_received = Message.count_messages({'id':session['user_id']})
    nbr_sent = Message.count_messages_sent({'id':session['user_id']})
    all_users = User.get_all_users({'id':session['user_id']})
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html",user = logged_user, msgs=messages,nb_sent=nbr_sent[0]['nbr_msg'], nb=nbr_received[0]['nbr_msg'],users=all_users)



@app.route('/users/create', methods=['POST'])
def register():
    if User.validate_register(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data_dict = {
            **request.form,
            'password':pw_hash
        }
        user_id = User.create(data_dict)
        session['user_id'] = user_id
        return redirect('/dashboard')
    return redirect('/')

@app.route('/login', methods =['POST'])
def login():
    user_from_db = User.get_by_email({'email':request.form['email']})
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            flash("Wrong Password !!!","login")
            return redirect('/')
        session['user_id'] = user_from_db.id
        return redirect('/dashboard')
    flash("Wrong email !!!!","login")
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')
