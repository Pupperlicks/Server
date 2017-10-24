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
    def get(self):
        """Return all rat sightings."""
        conn = e.connect()
        return {'sigtings': jsonify_row(conn.execute("select * from sightings"))}

    def post(self):
        """Execute an INSERT INTO sightings based on request JSON."""
        conn = e.connect()
        unique_key = request.json["Unique Key"]
        created_date = request.json["Created Date"]
        closed_date = request.json["Closed Date"]
        agency = request.json["Agency"]
        agency_name = request.json["Agency Name"]
        complaint_type = request.json["Complaint Type"]
        descriptor = request.json["Descriptor"]
        location_type = request.json["Location Type"]
        incident_zip = request.json["Incident Zip"]
        incident_address = request.json["Incident Address"]
        street_name = request.json["Street Name"]
        cross_street_1 = request.json["Cross Street 1"]
        intersection_street_1 = request.json["Intersection Street 1"]
        intersection_street_2 = request.json["Intersection Street 2"]
        address_type = request.json["Address Type"]
        city = request.json["City"]
        landmark = request.json["Landmark"]
        facility_type = request.json["Facility Type"]
        status = request.json["Status"]
        due_date = request.json["Due Date"]
        resolution = request.json["Resolution Action Updated Date"]
        community_board = request.json["Community Board"]
        borough = request.json["Borough"]
        x_coord = request.json["X Coordinate (State Plane)"]
        y_coord = request.json["Y Coordinate (State Plane)"]
        park_facility_name = request.json["Park Facility Name"]
        park_borough = request.json["Park Borough"]
        school_name = request.json["School Name"]
        school_number = request.json["School Number"]
        school_region = request.json["School Region"]
        school_code = request.json["School Code"]
        school_phone_number = request.json["School Phone Number"]
        school_address = request.json["School Address"]
        school_state = request.json["School State"]
        school_zip = request.json["School Zip"]
        school_not_found = request.json["School Not Found"]
        school_or_citywide_complaint = request.json["School or Citywide Complaint"]
        vehicle_type = request.json["Vehicle Type"]
        taxi_company = request.json["Taxi Company"]
        taxi_pick_up_location = request.json["Taxi Pick Up Location"]
        bridge_highway_name = request.json["Bridge Highway Name"]
        bridge_highway_direction = request.json["Bridge Highway Direction"]
        road_ramp = request.json["Road Ramp"]
        bridge_highway_segment = request.json["Bridge Highway Segment"]
        garage_lot_name = request.json["Garage Lot Name"]
        ferry_direction = request.json["Ferry Direction"]
        ferry_terminal_name = request.json["Ferry Terminal Name"]
        latitude = request.json["Latitude"]
        longitude = request.json["Longitude"]
        location = request.json["location"]
        try:
            query = conn.execute("INSERT INTO sightings values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}','{30}','{31}','{32}','{33}','{34}','{35}','{36}','{37}','{38}','{39}','{40}','{41}','{42}','{43}','{44}','{45}','{46}','{47}','{48}','{49}',)".format(unique_key,created_date, closed_date, agency, agency_name, complaint_type, descriptor, location_type, incident_zip, incident_address, street_name, cross_street_1, intersection_street_1, intersection_street_2, address_type, city, landmark, facility_type, status, due_date, resolution, community_board, borough, x_coord, y_coord, park_facility_name, park_borough, school_name, school_number, school_region, school_code, school_phone_number, school_address, school_state, school_zip, school_not_found, school_or_citywide_complaint, vehicle_type, taxi_company, taxi_pick_up_location, bridge_highway_name, bridge_highway_direction, road_ramp, bridge_highway_segment, garage_lot_name, ferry_direction, ferry_terminal_name, latitude, longitude, location))
            return {'status':'success'}
        except:
            return {'status':'failure'}

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
        return {'sigtings': jsonify_row(conn.execute("select * from sightings LIMIT 50"))}


api.add_resource(Sightings_50, '/50_sightings')
api.add_resource(Sightings, '/sightings')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
