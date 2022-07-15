# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
# model the class after the dojo table from our database

DATABASE = "dojo_and_ninjas"

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( Dojo(dojo) )
        return dojos

    # ! CREATE
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db( query, data)
    
    # ! READ/RETRIEVE TWO
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # Iterate over the db results and create instances of dojos with cls.
        dojo = Dojo(results[0])
        return dojo

    @classmethod
    def get_join(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])
        for result in results:
            dojo_ninja = {
                'id': result['ninjas.id'],
                'first_name': result['first_name'],
                'last_name': result['Last_name'],
                'age': result['age'],
                'dojo_id' : result['dojo_id'],
                'created_at': result['ninjas.created_at'],
                'updated_at': result['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(dojo_ninja))
            print(dojo)
        return dojo

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(fname)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data)