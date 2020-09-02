import numpy as np
import pandas as pd 
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify

#hawaii_path = "~/desktop/projects/Gitclone/Repo/10-Advanced-Data-Storage-and-Retrieval/Homework/Instructions/Resources/hawaii.sqlite"

hawaii_path = "../../Resources/hawaii.sqlite"

engine_hawaii = create_engine(f"sqlite:///{hawaii_path}")

Base = automap_base()

Base.prepare(engine_hawaii, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station 

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return(
        f"Welcome to my 'Home' page!<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
    )



## 4. Define what to do when a user hits the /about route
#@app.route("/about")
#def about():
    #print("Server received request for 'About' page...")
    ##=return "Welcome to my 'About' page!"


#5. Define what to do when a user hits the precipitation route
#@app.route(/api/v1.0/precipitation)

#@app.route("/api/v1.0/stations")
#def stations():
    #session = Session(engine)

    #results = session.query(Measurement.station).all()

    #session.close()



#XXX = [{}]

#@app.route(/api/v1.0/stations)
#def station_results
    #return jsonify(XXX)

#/api/v1.0/<start>

#/api/v1.0/<start>/<end





#Create an app, being sure to pass __name__
#app = Flask(__name__)


# Define what to do when a user hits the index route


if __name__ == "__main__":
    app.run(debug=True)
