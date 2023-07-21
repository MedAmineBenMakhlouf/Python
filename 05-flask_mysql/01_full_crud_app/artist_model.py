from mysqlconnection import connectToMySQL
class Artist:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.nationality = data_dict['nationality']
        self.rate = data_dict['rate']
        self.image = data_dict['image']
        self.is_dead = data_dict['is_dead']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM artists;"
        result = connectToMySQL("artists-schema").query_db(query)
        # print (result)
        all_artists= []
        for row in result:
            artist = cls(row)
            all_artists.append(artist)
        # print (all_artists)
        return all_artists
    
    @classmethod
    def create_artist(cls,data_dict):
        query = """
                    INSERT INTO artists(first_name,last_name, nationality,rate, image, is_dead)
                    values(%(first_name)s,%(last_name)s,%(nationality)s,%(rate)s,%(image)s,%(is_dead)s);
                """
        result = connectToMySQL("artists-schema").query_db(query,data_dict)
        return None