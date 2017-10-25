from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

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
	""""Create a dict with the object names + objects for a given SQLite query."""
    return [dict(zip(tuple(query.keys()), i)) for i in query.cursor]


class Sightings(Resource):
    def get(self):
        """Return all rat sightings."""
        conn = e.connect()
        return {'sightings': jsonify_row(conn.execute("select * from sightings"))}

    def post(self):
        """Execute an INSERT INTO sightings based on request JSON."""
        conn = e.connect()
        INSERT_SQL = f"""INSERT INTO sightings({','.join(FIELDS)}) VALUES({','.join("?"*len(FIELDS)})"""
        query = conn.execute(INSERT_SQL, request.json)

    def delete(self):
        """Execute a DELETE based on a given unique key."""
        conn = e.connect()
        unique_key = request.json["Unique Key"]
        try:
            query =  conn.execute("DELETE FROM SIGHTINGS WHERE Name=?", (unique_key,))
            return {'status':'success'}
        except:
            return {'status':'failure'}
       

class Sightings_50(Resource):
	"""A special class just to get the first 50 sightings."""
    def get(self):
        """Return the first 50 sightings of rats."""
        conn = e.connect()
        return {'sightings': jsonify_row(conn.execute("select * from sightings LIMIT 50"))}


api.add_resource(Sightings_50, '/50_sightings')
api.add_resource(Sightings, '/sightings')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
