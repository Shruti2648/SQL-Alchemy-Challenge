# Import dependencies:
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

# Database setup:
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare base and reflect tables:
Base = automap_base()
Base.prepare(engine,reflect=True)

# Save references to the tables:
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask setup:
app = Flask(__name__)

# Routes:

@app.route("/")
def welcome():
    return (
        f"Welcome to the Honolulu, HI Climate API! Please use the following routes tp navigate this API:<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session.engine()
    prcp_data = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    prcp_dict = defaultdict(list)
    for i, j in prcp_data:
        prcp_dict[i].append(j)

    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session.engine()
    station_data = session.query(Stations.station).all()
    session.close()

    station_names = list(np.ravel(station_data))

    return jsonify(station_names)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session.engine()
    tobs_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').all()
    session.close()

    tobs_dict = defaultdict(list)
    for i, j in tobs_data:
        prcp_dict[i].append(j)

    return jsonify(tobs_dict)
