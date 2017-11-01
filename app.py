from json import dumps

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from dateutil.parser import *
from datetime import *

# Create a engine for connecting to SQLite3.
# Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///sightings.db')

app = Flask(__name__)
api = Api(app)

# The columns in the database & our fields.
FIELDS = ["ferry_direction", "facility_type", "city", "resolution", "complaint_type", "intersection_street_1",
          "cross_street_2", "agency_name", "taxi_company", "longitude", "vehicle_type", "school_number",
          "street_name", "descriptor", "bridge_highway_segment", "agency", "school_or_citywide_complaint",
          "garage_lot_name", "cross_street_1", "community_board", "closed_date", "school_not_found",
          "park_borough", "location", "school_city", "due_date", "x_coord", "school_region", "created_date",
          "borough", "taxi_pick_up_location", "address_type", "intersection_street_2", "ferry_terminal_name",
          "road_ramp", "park_facility_name", "bridge_highway_name", "school_state", "school_zip", "school_address",
          "school_name", "latitude", "school_code", "incident_address", "location_type", "landmark", "y_coord",
          "unique_key", "bridge_highway_direction", "status", "incident_zip", "school_phone_number"]


def jsonify_row(query):
    """Create a dict with the object names + objects for a given SQLite query."""
    return [dict(zip(tuple(query.keys()), i)) for i in query.cursor]


class Sightings(Resource):
    # A class for rat sightings. Allows for one to get, post, and delete
    # sightings.

    def get(self):
        """Return all rat sightings."""
        conn = e.connect()
        return {'sightings': jsonify_row(conn.execute("select * from sightings"))}, 200

    def post(self):
        # Execute an INSERT INTO sightings based on request JSON.
        conn = e.connect()
        query = conn.execute("""INSERT INTO sightings({','.join(FIELDS)}) VALUES({','.join("?"*len(FIELDS))})""", request.json)
        return {'status': 'success'}, 201

    def delete(self):
        # Execute a DELETE based on a given unique key.
        conn = e.connect()
        unique_key = request.json["unique_key"]
        try:
            query = conn.execute(
                "DELETE FROM SIGHTINGS WHERE Name=?", (unique_key,))
            return {'status': 'success'}, 200
        except:
            return {'status': 'failure'}, 500


class Sightings_50(Resource):
    # A special class just to get the first 50 sightings.

    def get(self):
        # Return the first 50 sightings of rats.
        conn = e.connect()
        return {'sightings': jsonify_row(conn.execute("select * from sightings LIMIT 50"))}, 200

class Sightings_Range(Resource):
    # A class to retrieve all sightings that fall between two dates.

    def post(self):
        start_date = request.json["start_date"]
        end_date = request.json["end_date"]
        conn = e.connect()
        return {'sightings': jsonify_row(conn.execute('select * from sightings WHERE created_date BETWEEN "%s" AND "%s"' % (start_date, end_date)))}, 200


api.add_resource(Sightings_50, '/50_sightings')
api.add_resource(Sightings, '/sightings')
api.add_resource(Sightings_Range, '/range')

if __name__ == '__main__':
    app.run(host='0.0.0.0')