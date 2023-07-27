from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from flask import flash
#from flask_app.models.ninja import Ninja
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
    
    
    @staticmethod
    def validation_registration(data_dict):
        is_valid=True
        if len(data_dict['first_name'])<2:
            flash("first name must more then two character", "register")
            is_valid=False
        if len(data_dict['first_name'])==0:
            flash("first name must not be empty", "register")
            is_valid=False
        if len(data_dict['last_name'])<2:
            flash("last name mast be more then two", "register")
            is_valid=False
        if len(data_dict['last_name'])==0:
            flash("last name must not be empty", "register")
            is_valid=False
        if not EMAIL_REGEX.match(data_dict['email']):
            flash("your email is not valid", "register")
            is_valid=False
        if not re.search(r'\d', data_dict['password']):
            flash("your password must include a number", "register")
            is_valid=False
        if not re.search(r'[A-Z]', data_dict['password']):
            flash("your password must include a uppercase letter", "register")
            is_valid=False
        if data_dict['password'] != data_dict['confirm_password']:
            flash("password doesn't much", "register")
            is_valid=False
        if User.get_by_email({'email':data_dict['email']}):
            flash("user already exist", "register")
            is_valid=False
        return is_valid
    
    @classmethod
    def get_by_email(cls,data_dict):
        query=""" SELECT * FROM users WHERE email=%(email)s"""
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_by_id(cls,data_dict):
        query=""" SELECT * FROM users WHERE id=%(id)s"""
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        return cls(result[0])