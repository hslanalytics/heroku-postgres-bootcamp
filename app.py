# import necessary libraries
from models import create_classes
import os
import psycopg2
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
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("://", "ql://", 1)

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

tv_watched = create_classes(db)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Load Database from Static File
@app.route("/get", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["name"]
        hours = request.form["hours"]

        tv = tv_watched(name=name, hours=hours)
        db.session.add(tv)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")


@app.route("/api/tv")
def watched():
    results = db.session.query(tv_watched.name, tv_watched.hours).all()

    name_text = [result[0] for result in results]
    tv_text = [result[1] for result in results]

    tv_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": 0.0,
        "lon": 0.0,
        "text": name_text,
        "tv_text": tv_text,
        "hoverinfo": "text",
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(tv_data)


# # Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["petName"]
#         lat = request.form["petLat"]
#         lon = request.form["petLon"]

#         pet = Pet(name=name, lat=lat, lon=lon)
#         db.session.add(pet)
#         db.session.commit()
#         return redirect("/", code=302)

#     return render_template("form.html")


# @app.route("/api/pals")
# def pals():
#     results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

#     hover_text = [result[0] for result in results]
#     lat = [result[1] for result in results]
#     lon = [result[2] for result in results]

#     pet_data = [{
#         "type": "scattergeo",
#         "locationmode": "USA-states",
#         "lat": lat,
#         "lon": lon,
#         "text": hover_text,
#         "hoverinfo": "text",
#         "marker": {
#             "size": 50,
#             "line": {
#                 "color": "rgb(8,8,8)",
#                 "width": 1
#             },
#         }
#     }]

#     return jsonify(pet_data)


if __name__ == "__main__":
    app.run()
