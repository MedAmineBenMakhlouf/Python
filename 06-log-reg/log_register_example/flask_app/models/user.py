from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME 
from flask import flash
# from flask_app.models.ninja import Ninja
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.cretaed_at = data_dict['cretaed_at']
        self.updated_at = data_dict['updated_at']
        
    @classmethod
    def create(cls,data_dict):
        query= """INSERT INTO users (first_name,last_name,email,password) VALUES 
                (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def get_by_email(cls,data_dict):
        query="""SELECT * FROM users WHERE email=%(email)s;"""
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        print(result)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_by_id(cls,data_dict):
        query="""SELECT * FROM users WHERE id=%(id)s;"""
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        return cls(result[0])
    
    @staticmethod
    def validate_register(data_dict):
        is_valid=True
        if len(data_dict['first_name'])<2:
            flash("first name too short", "register")
            is_valid=False
        if len(data_dict['last_name'])<2:
            flash("last name too short", "register")
            is_valid=False
        if len(data_dict['password'])<7:
            flash("password too short", "register")
            is_valid=False
        elif data_dict['password'] != data_dict['confirm_password']:
            flash("password and Confirm password don't match")
            is_valid=False
        if not EMAIL_REGEX.match(data_dict['email']):
            flash("invalid mail address", "register")
            is_valid=False
        elif User.get_by_email({'email':data_dict['email']}):
            flash("email already taken", "register")
            is_valid=False
        return is_valid
    
    # @staticmethod
    # def validate_login(data_dict):
    #     is_valid=True
    #     user_from_db = User.get_by_email({'email':data_dict['email']})
    #     if not user_from_db:
    #         flash("Email not")
    #         is_valid=False
    #         return is_valid
    