from mysqlconnection import connectToMySQL
class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def get_all(cls):
        query = """
        SELECT id,first_name, last_name,email,DATE_FORMAT(created_at, '%M %e, %Y') as created_at,updated_at FROM users;
        """
        result = connectToMySQL("users_schema").query_db(query)
        all_users= []
        for row in result:
            user = cls(row)
            all_users.append(user)
        return all_users
    
    @classmethod
    def create_user(cls,data_dict):
        query= """
                INSERT INTO users(first_name,last_name,email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s);
                """
        result = connectToMySQL('users_schema').query_db(query,data_dict)
        return None