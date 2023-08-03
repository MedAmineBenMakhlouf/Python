from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
#from flask_app.models.ninja import Ninja
from flask import flash

class Recipe:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.name = data_dict['name']
        self.description = data_dict['description']
        self.instructions = data_dict['instructions']
        self.date_cooked = data_dict['date_cooked']
        self.under_30_minutes = data_dict['under_30_minutes']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.creator =""
        
    @classmethod
    def get_user_recipe(cls,data_dict):
        query="""SELECT * from recipes
                    join users on users.id=recipes.user_id
                    where recipes.id=%(id)s"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        print(results)
        recipes = Recipe(results[0])
        for row in results:
            recipes.creator = row['first_name']
        return recipes
    
    @classmethod
    def get_recipe(cls,data_dict):
        query="""SELECT * from recipes
                    where id=%(id)s"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        recipes = Recipe(results[0])
        return recipes
    
    @staticmethod
    def validate_recipe(data_dict):
        is_valid = True
        if len(data_dict['name'])< 2:
            flash("Name too short .....", "name")
            is_valid = False
        if len(data_dict['description'])< 2:
            flash("Last Name too short .....", "description")
            is_valid = False
        if len(data_dict['instructions'])< 2:
            flash("Last Name too short .....", "instructions")
            is_valid = False
        if 'under_30_minutes' not in data_dict:
            flash("Please put yes or no", "under_30_minutes")
            is_valid = False
        if not data_dict['date_cooked']:
            flash("please put your age", "date_cooked")
            is_valid=False
        return is_valid
    
    @classmethod
    def create_recipe(cls,data_dict):
        query="""INSERT INTO recipes (user_id,name,description,instructions,date_cooked,under_30_minutes)
                    VALUES (%(user_id)s,%(name)s,%(description)s,%(instructions)s,%(date_cooked)s,%(under_30_minutes)s)"""
                    
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def update_recipe(cls,data_dict):
        query= """UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,
                    date_cooked=%(date_cooked)s,under_30_minutes=%(under_30_minutes)s WHERE id=%(id)s"""
                    
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def delete(cls,data_dict):
        query = """delete from recipes where id=%(id)s"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)