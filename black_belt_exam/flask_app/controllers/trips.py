from flask import  render_template, redirect, request, flash,session
from flask_app import app
from flask_app.models.trip import Trip
from flask_app.models.user import User
from datetime import datetime


@app.route('/trips/new')
def recipe_new():
    if not 'user_id' in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("create_trip.html",user=logged_user)

@app.route('/trips/create', methods=['POST'])
def create_recipe():
    if Trip.validate_trip(request.form):
        data_dict = {
            **request.form,
            'user_id': session['user_id']
        }
        Trip.create_trip(data_dict)
        return redirect('/dashboard')
    return redirect('/trips/new')

@app.route('/trips/<int:trip_id>')
def details_trip(trip_id):
    if not 'user_id' in session:
        return redirect('/')
    user_trip = Trip.get_user_trip({'id':trip_id})
    user = User.get_by_id({'id':session['user_id']})
    user_joined = Trip.get_details_user_joined()
    return render_template('details.html',user=user_trip,this_user=user,userjoined=user_joined)

@app.route('/trips/<int:trip_id>/edit')
def edit_recipe(trip_id):
    if 'user_id' not in session:
        return render_template('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    user_trip = Trip.get_trip({'id':trip_id})
    return render_template('edit_trip.html',trip=user_trip,user=logged_user)

@app.route('/trips/<int:trip_id>/update', methods=['POST'])
def update_trip(trip_id):
    if Trip.validate_trip(request.form):
        data = {
            **request.form,
            'id':trip_id
        }
        Trip.update_trip(data)
        return redirect('/dashboard')
    return redirect(f'/trips/{trip_id}/edit')

@app.route('/trips/<int:trip_id>/destroy', methods=['POST'])
def delete(trip_id):
    if 'user_id' not in session:
        return render_template('/')
    Trip.delete({'id':trip_id})
    return redirect('/dashboard')



@app.route('/trips/join/<int:trip_id>', methods=['POST'])
def joinTrip(trip_id):
    if 'user_id' not in session:
        return render_template('/')
    Trip.jointrip({'trip_id':trip_id,'user_id':session['user_id']})
    return redirect('/dashboard')



@app.route('/trips/cancel/<int:trip_id>/destroy', methods=['POST'])
def joindelete(trip_id):
    if 'user_id' not in session:
        return render_template('/')
    Trip.Joindelete({'trip_id':trip_id})
    return redirect('/dashboard')