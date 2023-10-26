from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from datetime import datetime
# from flask_app.models.trip import Trip
from flask import flash

class Trip:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.destination = data_dict['destination']
        self.start_date = data_dict['start_date']
        self.end_date = data_dict['end_date']
        self.plan = data_dict['plan']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.creator =""
    
    @classmethod
    def get_all_user_trip(cls,data_dict):
        query="""SELECT * from trips JOIN users on trips.user_id = users.id 
                    WHERE trips.user_id=%(id)s order by trips.id desc;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        trips = []
        for row in results:
            trip = cls(row)
            trip.creator = f"{row['first_name']}"
            trips.append(trip)
        return trips
    
    @classmethod
    def get_other_user_trip(cls,data_dict):
        query="""SELECT * from trips 
                    LEFT JOIN usersjointrips on usersjointrips.trip_id = trips.id
                    LEFT JOIN users on users.id = usersjointrips.user_id 
                    WHERE usersjointrips.trip_id!=%(id)s order by trips.id desc;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        trips = []
        for row in results:
            trip = cls(row)
            trip.creator = f"{row['first_name']}"
            trips.append(trip)
        return trips
    
    @classmethod
    def get_not_user_trip(cls,data_dict):
        query="""SELECT * from trips
                    LEFT JOIN users on users.id = trips.user_id 
                    WHERE users.id!=%(id)s order by trips.id desc;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        trips = []
        for row in results:
            trip = cls(row)
            trip.creator = f"{row['first_name']}"
            trips.append(trip)
        return trips
        
    @classmethod
    def get_user_trip(cls,data_dict):
        query="""SELECT * from trips
                    join users on users.id=trips.user_id
                    where trips.id=%(id)s order by trips.id desc;"""
                    
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        trips = cls(results[0])
        trips.start_date = datetime.strftime(results[0]['start_date'],'%m/%d/%y')
        trips.end_date = datetime.strftime(results[0]['end_date'], '%m/%d/%y')
        trips.created_at = datetime.strftime(results[0]['created_at'],'%m/%d/%y')
        trips.updated_at = datetime.strftime(results[0]['updated_at'], '%m/%d/%y')
        for row in results:
            trips.creator = row['first_name']
            
        return trips
    
    @classmethod
    def get_trip(cls,data_dict):
        query="""SELECT * from trips
                    where id=%(id)s"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        trip = cls(results[0])
        return trip
    
    @classmethod
    def get_details_user_joined(cls):
        query= """select * from users 
        LEFT JOIN usersjointrips on users.id= usersjointrips.user_id
        LEFT JOIN trips on trips.id = usersjointrips.trip_id;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        all_users=[]
        for row in results:
            users = cls(row)
            all_users.append(users)
        return all_users
    
    @staticmethod
    def validate_trip(data_dict):
        is_valid = True
        if data_dict['start_date']=="":
            flash("start date is required!!", "start_date")
            is_valid = False
        elif datetime.strptime(data_dict['start_date'], '%Y-%m-%d').date()<datetime.now().date():
            flash("date trip must not be in the past", "start_date")
            is_valid=False
        if data_dict['end_date']=="":
            flash("please put the end of the trip", "end_date")
            is_valid=False
        elif datetime.strptime(data_dict['start_date'], '%Y-%m-%d').date()>datetime.strptime(data_dict['end_date'], '%Y-%m-%d').date():
            flash("end of the trip must be superior to start date of trip", "end_date")
            is_valid=False
        if len(data_dict['plan'])<3:
            flash("plan must be more then 7 characters", "plan")
            is_valid=False
        if len(data_dict['destination'])<3:
            flash("destination name is to short", "destination")
            is_valid=False
        return is_valid
    
    @classmethod
    def create_trip(cls,data_dict):
        query="""INSERT INTO trips (user_id,destination,start_date,end_date,plan)
                    VALUES (%(user_id)s,%(destination)s,%(start_date)s,%(end_date)s,%(plan)s);"""
                    
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def jointrip(cls,data_dict):
        query="""INSERT INTO usersjointrips (user_id,trip_id)
                    VALUES (%(user_id)s,%(trip_id)s);"""
                    
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    
    @classmethod
    def update_trip(cls,data_dict):
        query= """UPDATE trips SET destination=%(destination)s,start_date=%(start_date)s,end_date=%(end_date)s,
                    plan=%(plan)s WHERE id=%(id)s;"""
                    
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def delete(cls,data_dict):
        query = """delete from trips where id=%(id)s;"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def Joindelete(cls,data_dict):
        query = """delete from usersjointrips where trip_id=%(trip_id)s;"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    
    
    
    