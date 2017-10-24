# Pupperlicks Server

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