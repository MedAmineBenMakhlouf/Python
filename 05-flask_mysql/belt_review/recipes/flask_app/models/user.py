from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from flask_app.models.recipe import Recipe
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.recipes = {}

    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users 
                    (first_name, last_name, email, password)
                    VALUES 
                    (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        return connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
    
    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM users WHERE id =%(id)s;"""
        result = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data_dict):
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        result = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        if result:
            return cls(result[0])
        return False
    
    # @classmethod
    # def get_all_users(cls,data_dict):
    #     query="select * from users where id!=%(id)s"
    #     results = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
    #     print(results)
    #     users = []
    #     if results:
    #         for user in results:
    #             users.append(cls(user))
    #     return users
    
    @classmethod
    def get_all_user_recipes(cls):
        query="""SELECT * from users
                    join recipes on users.id=recipes.user_id"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        users =[]
        for row in results:
            data_user = {
                "id": row["id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            user = cls(data_user)
            user.recipes = {
                "id": row["recipes.id"],
                "user_id": row["user_id"],
                "name": row["name"],
                "description": row["description"],
                "instructions": row["instructions"],
                "under_30_minutes": row["under_30_minutes"],
                "date_cooked": row["date_cooked"],
                "created_at": row["recipes.created_at"],
                "updated_at": row["recipes.updated_at"]
            }
            
            users.append(user)
            
            
        print(users)
        return users
    
    # @classmethod
    # def get_user_recipe(cls,data_dict):
    #     query="""SELECT * from recipes
    #                 join users on users.id=recipes.user_id
    #                 where recipes.id=%(id)s"""
    #     results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    #     recipes = Recipe(results[0])
    #     return recipes
    
    @staticmethod
    def validate_register(data_dict):
        is_valid = True
        if len(data_dict['first_name'])< 2:
            flash("First Name too short .....", "first_name")
            is_valid = False
        if len(data_dict['last_name'])< 2:
            flash("Last Name too short .....", "last_name")
            is_valid = False
        if len(data_dict['password'])< 7:
            flash("Password too short .....", "password")
            is_valid = False
        elif data_dict['password'] != data_dict['confirm_password']:
            flash("Password and Confirm password Don't match !!!!!", "password")
            is_valid = False
        if not EMAIL_REGEX.match(data_dict['email']): 
            flash("Invalid email address!", "email")
            is_valid = False
        elif User.get_by_email({'email':data_dict['email']}):
            flash("Email Already taken . Hope by you !!!! ", "email")
            is_valid = False
        return is_valid
    