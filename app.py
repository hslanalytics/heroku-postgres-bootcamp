# import necessary libraries
from models import create_classes, create_tv_watched_geo
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy

# DATABASE_URL is automatically populated from Heroku
# Removed SQLite connection as this example connects to postgres
# .replace("://", "ql://", 1) addresses Heroku dialect mismatch
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("://", "ql://", 1)

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

tv_watched = create_classes(db)
tv_watched_geo = create_tv_watched_geo(db)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# @TODO: Route needed for each dataset
# Example 1: Two column table
@app.route("/api/tv.json")
def watched():
    results = db.session.query(tv_watched.name, tv_watched.hours).all()

    name_text = [result[0] for result in results]
    hours = [result[1] for result in results]

    tv_data = [{
        "name": name_text,
        "hours": hours
    }]

    return jsonify(tv_data)

if __name__ == "__main__":
    app.run()


@app.route("/api/tv_geo.json")
def watched_geo():
    
    # Query all columns in class
    results = db.session.query(tv_watched_geo).all()

    all_tv_watched_geo = []

    # Loop through all records and add to dict
    for result in results:

        tv_watched_geo_dict = {}

        tv_watched_geo_dict["name"] = result.name
        tv_watched_geo_dict["hours"] = result.hours
        tv_watched_geo_dict["lat"] = result.lat
        tv_watched_geo_dict["lon"] = result.lon

        all_tv_watched_geo.append(tv_watched_geo_dict)

    json_tv_watched_geo = {"data": {"tv_watched": all_tv_watched_geo}}

    return jsonify(json_tv_watched_geo)
