from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine=create_engine("sqlite:///hawaii.sqlite")
Base=automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
session=Session(engine)
Measurement = Base.classes.Measurement
Stations= Base.classes.Stations

app= Flask(__name__)
#Have to figure out error for below
@app.route("/api/v1.0/precipitation")
def precipitation():
   measurement_results=[]
   #Query all Measurement
   results = session.query(Measurement).all()   
   for data in results:
       measurement_dict={}
       measurement_dict["date"] = data.date
       measurement_dict["tobs"] = data.tobs
       all_results.append(measurement_dict)  
   return jsonify(all_results)

@app.route("/api/v1.0/stations")
def stations():
    results=session.query(Stations.station).all()
    all_stations=list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temperatures():
    results=session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2017-04-08').all()
    all_temperatures=list(np.ravel(results))
    return jsonify(all_temperatures)

@app.route("/api/v1.0/2017-07-15/2017-07-25")
def calc_temp():
    results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs), func.avg(Measurement.tobs)
                                      ).filter(Measurement.date.between('2017-07-15','2017-07-25')).all()
    vacation_temps = list(np.ravel(results))
    return jsonify(vacation_temps)

@app.route("/api/v1.0/2017-07-15")
def start_temp():
    results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs), func.avg(Measurement.tobs)
                                      ).filter(Measurement.date >='2017-07-15').all()
    vacation_start = list(np.ravel(results))
    return jsonify(vacation_start)
if __name__ == '__main__':
    app.run(debug=True)