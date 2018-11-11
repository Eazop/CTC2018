import Location
import requests
import json

apiKey = "AIzaSyCbboNhiFtxSQu5SsdhTRhC3O1cq3MaHE4"

class NearByLocations:
    endpoint = ""
    userLocation = None
    locations = list()
    def findServices(self, town, service):
        resp = requests.get("https://maps.googleapis.com/maps/api/geocode/json?parameters")
        locations = list()
        if service == "Naloxone":
            endpoint = "https://data.ct.gov/resource/4vs4-3cb3.json?City=" +town.upper()
            resp = requests.get(endpoint)
            result = json.loads(resp.content)
            if resp == "":
                return 0
            for entry in result:
                l = Location.Location()
                l.init(entry['pharmacy_name'], entry['phone'], entry['location_1'], entry['address'], entry['city'], entry['zip'], "Naloxone")
                self.locations.append(l)
        elif service == "Drop Box":
            endpoint = "https://data.ct.gov/resource/5e4g-stz3.json?City=" + town.upper()
            resp = requests.get(endpoint)
            result = json.loads(resp.content)
            for entry in result:
                l = Location.Location()
                l.init(entry['location_name'], "", entry['location_1'], entry['address'], entry['city'], "", service)
                self.locations.append(l)
        elif service == "Care Facilities":
            endpoint = "https://data.ct.gov/resource/htz8-fxbk.json?City="+ town.upper()
            resp = requests.get(endpoint)
            result = json.loads(resp.content)
            for entry in result:
                l = Location.Location()
                l.init(entry['name'], "", "", entry['address'], entry['city'], entry['zip'], service)
                self.locations.append(l)
        else:
            return 0


