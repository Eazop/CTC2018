import Location
import requests
import json

apiKey = "AIzaSyCbboNhiFtxSQu5SsdhTRhC3O1cq3MaHE4"

class NearByLocations:
    endpoint = ""
    userLocation = None
    locations = list()
    def findServices(self, town, service):
        locations = list()
        if service == "Naloxone":
            endpoint = "https://data.ct.gov/resource/4vs4-3cb3.json?City=" +town.upper()
            resp = requests.get(endpoint)
            result = json.loads(resp.content)
            if resp == "":
                return 0
            for entry in result:
                phone = ""
                l = Location.Location()
                if 'phone' in list(entry):
                    phone = entry['phone']
                if not ('coordinates'  in list(entry)):
                    address = entry['address'].replace(" ", "+")
                    city = entry['city']
                    resp = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + address + ",+" + city + ",+CT&key=AIzaSyBudLNw6Yc7FCyOS72H7-0PcxkHTrGlYGc")
                    rest = json.loads(resp.content)
                    coords = {'coordinates': (rest['results'][0]['geometry']['location']['lng'], rest['results'][0]['geometry']['location']['lat'])}
                else:
                    coords = entry['location_1']

                l.init(entry['pharmacy_name'], phone, coords, entry['address'], entry['city'], entry['zip'], "Naloxone")
                self.locations.append(l)
        elif service == "Drop Box":
            endpoint = "https://data.ct.gov/resource/5e4g-stz3.json?City=" + town.upper()
            resp = requests.get(endpoint)
            result = json.loads(resp.content)
            for entry in result:
                l = Location.Location()
                l.init(entry['location_name'], "", (entry['location_1']['latitude'], entry['location_1']['longitude']), entry['address'], entry['city'], "", service)
                self.locations.append(l)
        elif service == "Care Facilities":
            endpoint = "https://data.ct.gov/resource/htz8-fxbk.json?City="+ town.upper()
            resp = requests.get(endpoint)
            result = json.loads(resp.content)

            for entry in result:
                address = entry['address'].replace(" ", "+")
                city = entry['city']
                l = Location.Location()
                resp = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + address + ",+" + city + ",+CT&key=AIzaSyBudLNw6Yc7FCyOS72H7-0PcxkHTrGlYGc")
                rest = json.loads(resp.content)
                l.init(entry['name'], "", rest['results'][0]['geometry']['location'], entry['address'], entry['city'], entry['zip'], service)
                self.locations.append(l)
        else:
            return 0

