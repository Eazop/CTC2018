from flask import Flask, render_template, request, redirect
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_bootstrap import Bootstrap
from NearByLocations import NearByLocations

app = Flask(__name__, template_folder=".")
app.config['GOOGLEMAPS_KEY'] = ""
Bootstrap(app)
GoogleMaps(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    
    return render_template('example.html')

@app.route('/mapView/', methods=['GET', 'POST'])
def mapview():
    location = NearByLocations()
    location.findServices(request.form['Town'], request.form['Service'])

    # creating a map in the view
    mymap = Map(
        style = "height: 1000px; width: 1400px; margin: 0;",
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )

    return render_template('pages/index.html', mymap=mymap)

if __name__ == "__main__":
    app.run(debug=True)
