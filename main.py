from flask import Flask, render_template, request, redirect, session
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_bootstrap import Bootstrap
from NearByLocations import NearByLocations
import requests
import json

app = Flask(__name__, template_folder=".")
app.config['GOOGLEMAPS_KEY'] = "AIzaSyBudLNw6Yc7FCyOS72H7-0PcxkHTrGlYGc"
Bootstrap(app)
GoogleMaps(app)


app.config.update(dict(
DATABASE='',
SECRET_KEY='development key',
USERNAME='',
PASSWORD=''
))

@app.route("/", methods=['GET', 'POST'])
def index():
    session.permanent = False

    mymap = Map(
    style="width: 100vw; height: 100vh;",
    identifier="view-side",
    lat= 41.6032,
    lng=  -73.0877,
    markers=[],
    zoom=9
    )
    return render_template('pages/index.html', mymap=mymap)

@app.route('/mapView/', methods=['GET', 'POST'])
def mapview():
    location = NearByLocations()
    location.locations = []
    location.findServices(request.form['Town'], request.form['Service'])
    mymap = None
    if len(location.locations) == 0:
        mymap = Map(
            style="width: 100vw; height: 100vh;",
            identifier="view-side",
            lat= 41.6032,
            lng=  -73.0877,
            markers=[]
        )
    else:
        markers=[]
        if request.form['Service'] == "Care Facilities":
            for entry in location.locations:
                markers.append({
                    'icon': '/static/images/doc.png',
                    'lat': entry.location['lat'], 
                    'lng': entry.location['lng']
                    }
                    )
        elif request.form['Service'] == "Drop Box":
            for entry in location.locations:
                markers.append({
                    'icon': '/static/images/box.png',
                    'lat': entry.location[0], 
                    'lng': entry.location[1]
                    }
                    )
        else:
            for entry in location.locations:
                markers.append(
                    {
                    'icon': '/static/images/pharmacy.png',
                    'lat': entry.location['coordinates'][1], 
                    'lng': entry.location['coordinates'][0]
                    }
                    )
    # creating a map in the view
        mymap = Map(
            style="width: 100vw; height: 100vh;",
            identifier="view-side",
            lat= markers[0]['lat'],
            lng= markers[0]['lng'],
            markers=markers
        )
    return render_template('pages/index.html', mymap=mymap, prevValue=request.form['Town'])

#Later implemenatations
@app.route('/FAQ/')
def displayFacts():
    #do stuff

    return render_template('pages/index.html')


#Later implemenatations
@app.route('/Help/')
def displayHelp():
    #do stuff

    return render_template('pages/index.html')

#Later implemenatations
@app.route('/Prevention/')
def displayPrevention():
    #do stuff

    return render_template('pages/index.html')



if __name__ == "__main__":
    app.run(debug=True)
