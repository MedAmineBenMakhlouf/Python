from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
from flask_app import DATABASE_NAME
from flask_app.models.user import User
from flask import flash
import math

class Message:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.sender_id = data_dict['sender_id']
        self.receiver_id = data_dict['receiver_id']
        self.message = data_dict['message']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.sender = ""
        
        
    @classmethod
    def get_all_user_messages(cls,data_dict):
        query="""SELECT * from users
                    join tranfert_messages on users.id=tranfert_messages.sender_id
                    where tranfert_messages.receiver_id=%(id)s;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)

        messages=[]
        if results:
            
            for row in results:
                message_data = {
                    "id": row["tranfert_messages.id"],
                    "message": row["message"],
                    "sender_id": row['sender_id'],
                    "receiver_id": row['receiver_id'],
                    "created_at": row["tranfert_messages.created_at"],
                    "updated_at": row["tranfert_messages.updated_at"],
                }
                message = cls(message_data)
                message.sender = f"{row['first_name']} {row['last_name']}"
                messages.append(message)

        return messages
    
    @classmethod
    def send(cls,data_dict):
        query=""" INSERT INTO tranfert_messages (sender_id,receiver_id,message) 
                    VALUES (%(sender_id)s,%(receiver_id)s,%(message)s)"""
        
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def count_messages_sent(cls,data_dict):
        query="select count(*) as nbr_msg from tranfert_messages where sender_id=%(id)s"
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        if result:
            return result
        return 0
    
    @classmethod
    def count_messages(cls,data_dict):
        query="select count(*) as nbr_msg from tranfert_messages where receiver_id=%(id)s"
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        if result:
            return result
        return 0
    
    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

    @classmethod
    def delete(cls,data_dict):
        query="delete from tranfert_messages where id=%(id)s"
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)