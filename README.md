# Pupperlicks Server

![](https://i.pinimg.com/originals/a7/d6/d0/a7d6d0e99997fc4b6d7c2e120b73f185.gif)

## Notes
The database was populated on 10/24/17 by using the SQLite 3 CSV import utility. The database can be found in the home folder of the server named `sightings.db`. The server is a RESTful Flask implementation.

## Install
Make a virtualenv and then `sudo pip install -r requirements.txt`. You can then import the CSV to SQLite3 (put it in the same folder as your root directory) afterward running `python app.py` will run the server.

## Routes
**GET**
- `/50_sightings`
    - Returns the first 50 rat sightings from the database.

- `/sightings`
    - Returns all entries in the database.

**POST**
- `/sightings`
    - For the time being we allow the client to generate the `unique_key` but in API v1.1 this will be deprecated and replaced by server side generation. Posting a sighting with a format similar to that of the below will insert it into the database. The server will return the success of the operation.

    Sample insertion:
    ```json
    {
        "intersection_street_1":"TRINITY PLACE",
        "school_name":"Unspecified",
        "park_borough":"MANHATTAN",
        "borough":"MANHATTAN",
        "intersection_street_2":"RECTOR STREET",
        "bridge_highway_segment":"",
        "school_city":"Unspecified",
        "descriptor":"Rat Sighting",
        "school_zip":"Unspecified",
        "complaint_type":"Rodent",
        "closed_date":"9\/18\/2015 0:00",
        "incident_address":"",
        "due_date":"10\/4\/2015 15:01",
        "vehicle_type":"",
        "location_type":"3+ Family Mixed Use Building",
        "incident_zip":"10006",
        "street_name":"",
        "y_coord":"197137",
        "agency_name":"Department of Health and Mental Hygiene",
        "cross_street_1":"",
        "school_region":"Unspecified",
        "school_or_citywide_complaint":"",
        "garage_lot_name":"",
        "resolution":"9\/18\/2015 0:00",
        "school_state":"Unspecified",
        "school_number":"Unspecified",
        "taxi_company":"",
        "facility_type":"N\/A",
        "landmark":"",
        "community_board":"01 MANHATTAN",
        "school_phone_number":"Unspecified",
        "cross_street_2":"",
        "agency":"DOHMH",
        "road_ramp":"",
        "ferry_direction":"",
        "taxi_pick_up_location":"",
        "status":"Closed",
        "x_coord":"980656",
        "city":"NEW YORK",
        "unique_key":"31464015",
        "latitude":"40.70777155",
        "location":"(40.70777155363643, -74.01296309970473)",
        "address_type":"INTERSECTION",
        "bridge_highway_name":"",
        "longitude":"-74.0129631",
        "created_date":"9\/4\/2015 0:00",
        "ferry_terminal_name":"",
        "school_address":"Unspecified",
        "school_not_found":"N",
        "school_code":"Unspecified",
        "park_facility_name":"Unspecified",
        "bridge_highway_direction":""
    }
    ```
- `/range`
    - Give the endpoint 2 dates, as described in the following format and it will return all of the entries in the database that fall within that range.

    *Note*: Please only provide dates in the MM/DD/YYYY format. Nothing else will be (or is planned to be) supported.

    Sample request:
    ```json
    {
	    "start_date":"9/4/2015",
	    "end_date":"9/6/2015"
    }
    ```

**DELETE**
-  `/sightings`
    - A sample of valid JSON to send is below. Provide a `unique_key` for deletion and the server will return the success of the operation.
    ```json
    {
        "unique_key":"31464015"
    }
    ```
