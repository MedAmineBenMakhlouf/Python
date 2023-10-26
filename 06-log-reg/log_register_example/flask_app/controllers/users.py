from flask import  render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/')
def index():
    # all_dojos = Dojo.get_all()
    
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", user= logged_user)

@app.route('/users/create', methods=['POST'])
def register():
    print(request.form)
    if User.validate_register(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data_dict = {
            **request.form,
            'password':pw_hash
        }
        user_id = User.create(data_dict)
        session['user_id']=user_id
        return redirect('/dashboard')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    user_form_db = User.get_by_email({'email':request.form['email']})
    if user_form_db:
        if not bcrypt.check_password_hash(user_form_db.password, request.form['password']):
            flash("wrong password","login")
            return redirect('/')
        session['user_id'] = user_form_db.id
        return redirect('/dashboard')
    flash("email doesn't exist","login")
    return redirect("/")

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

