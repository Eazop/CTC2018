from flask import Flask, render_template, request, redirect, session
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_bootstrap import Bootstrap
from NearByLocations import NearByLocations

app = Flask(__name__, template_folder=".")
app.config['GOOGLEMAPS_KEY'] = ""
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
    return render_template('example.html')

@app.route('/mapView/', methods=['GET', 'POST'])
def mapview():
    location = NearByLocations()
    location.findServices(request.form['Town'], request.form['Service'])

    markers=[]
    for entry in location.locations:
        markers.append((entry.location['coordinates'][1], entry.location['coordinates'][0]))
    # creating a map in the view
    mymap = Map(
        style="width: 100vw; height: 100vh;",
        identifier="view-side",
        lat= location.locations[0].location['coordinates'][1],
        lng=  location.locations[0].location['coordinates'][0],
        markers=markers
    )

    return render_template('pages/index.html', mymap=mymap)

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
