from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# Create a engine for connecting to SQLite3.
# Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///sightings.db')

app = Flask(__name__)
api = Api(app)


def jsonify_row(query):
	""""Create a dict with the object names + objects for a given SQLite query."""
    return [dict(zip(tuple(query.keys()), i)) for i in query.cursor]


class Sightings(Resource):
	"""Return all rat sightings."""
    def get(self):
        conn = e.connect()
        return {'sigtings': jsonify_row(conn.execute("select * from sightings"))}


class Sightings_50(Resource):
	"""Return the first 50 sightings of rats."""
    def get(self):
        conn = e.connect()
        return {'sigtings': jsonify_row(conn.execute("select * from sightings LIMIT 50"))}

api.add_resource(Sightings_50, '/50_sightings')
api.add_resource(Sightings, '/sightings')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
