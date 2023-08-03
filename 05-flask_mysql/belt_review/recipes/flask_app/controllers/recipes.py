from flask import  render_template, redirect, request, flash,session
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from datetime import datetime


@app.route('/recipes/new')
def recipe_new():
    
    return render_template("create_recipe.html")

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if Recipe.validate_recipe(request.form):
        data_dict = {
            **request.form,
            'user_id': session['user_id']
        }
        Recipe.create_recipe(data_dict)
        return redirect('/recipes')
    return redirect('/recipes/new')

@app.route('/users/view/<int:user_recipes_id>')
def details_recipes(user_recipes_id):
    user_recipe = Recipe.get_user_recipe({'id':user_recipes_id})
    user = User.get_by_id({'id':session['user_id']})
    return render_template('details.html',user=user_recipe,this_user=user)

@app.route('/recipes/<int:user_recipes_id>/edit')
def edit_recipe(user_recipes_id):
    user_recipe = Recipe.get_recipe({'id':user_recipes_id})
    return render_template('edit_recipe.html',recipe=user_recipe)

@app.route('/recipes/<int:recipe_id>/update', methods=['POST'])
def update_recipe(recipe_id):
    data_dict = {
        **request.form,
        'id':recipe_id
    }
    recipe = Recipe.update_recipe(data_dict)
    return redirect('/recipes')

@app.route('/recipes/<int:user_recipes_id>/destroy')
def delete(user_recipes_id):
    recipe = Recipe.delete({'id':user_recipes_id})
    return redirect('/recipes')