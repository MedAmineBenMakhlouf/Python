from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from datetime import datetime
#from flask_app.models.ninja import Ninja
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create(cls,data_dict):
        query= """INSERT INTO emails (email) VALUES (%(email)s);
                """
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def get_by_id(cls,data_dict):
        query="""SELECT * FROM emails WHERE id=%(id)s;"""
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        print(result)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_by_email(cls,data_dict):
        query="""SELECT * FROM emails WHERE email=%(email)s;"""
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        print(result)
        if result:
            return cls(result[0])
        return False
    
    
    @classmethod
    def get_all(cls):
        query="""SELECT * FROM emails;"""
        results=connectToMySQL(DATABASE_NAME).query_db(query)
        all_mails=[]
        for row in results:
            date = row['created_at']
            email = cls(row)
            email.created_at = datetime.strftime(date, '%d %B %Y %I:%M %p')
            all_mails.append(email)
        return all_mails
    
    # @classmethod
    # def get_last_email(cls):
    #     query="""SELECT * FROM emails order by id desc limit 1;"""
    #     results=connectToMySQL(DATABASE_NAME).query_db(query)
        
    #     return cls(results[0])
    
    @classmethod
    def delete_email(cls,data_dict):
        query = "DELETE FROM emails WHERE id=%(id)s;"
        
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        
        
    @staticmethod
    def validate_email(data_dict):
        is_valid=True
        if not EMAIL_REGEX.match(data_dict['email']):
            flash("invalid mail address", "email")
            is_valid=False
        if Email.get_by_email({'email':data_dict['email']}):
            flash("email already taken", "email")
            is_valid=False
        
        return is_valid