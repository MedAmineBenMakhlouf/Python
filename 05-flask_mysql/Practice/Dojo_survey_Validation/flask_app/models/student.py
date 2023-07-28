from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
#from flask_app.models.ninja import Ninja
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Student:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.language = data_dict['language']
        self.location = data_dict['location']
        self.comments = data_dict['comments']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create(cls,data_dict):
        query= """INSERT INTO students (name,language,location,comments) VALUES 
                (%(name)s,%(language)s,%(location)s,%(comments)s);
                """
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def get_student_by_id(cls,data_dict):
        # query = """SELECT id,first_name, last_name,email, created_at, DATE_FORMAT(updated_at, '%M %e, %Y %h:%i %p') as updated_at 
        #         FROM users WHERE id=%(id)s;"""
        query = """SELECT * FROM students WHERE id=%(id)s;"""
        result = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        if result:
            the_user = cls(result[0])
            return the_user
        return False

    @staticmethod
    def validation(data_dict):
        is_valid=True
        if len(data_dict['name'])<2:
            is_valid = False
            flash("name is required", "name")
        if not data_dict['location']:
            is_valid = False
            flash("location is required", "location")
        if not data_dict['language']:
            is_valid = False
            flash("language is required", "language")
        if len(data_dict['comments'])<1:
            is_valid = False
            flash("comment is required", "comments")
        
        return is_valid
    
    
    # @classmethod
    # def get_all(cls):
    #     query = """ SELECT * FROM users;  """
        
    #     result = connectToMySQL(DATABASE_NAME).query_db(query)
    #     all_users= []
    #     for row in result:
    #         user = cls(row)
    #         all_users.append(user)
    #     return all_users