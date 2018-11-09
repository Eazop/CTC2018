import requests
import json
import RadiusLocator

resp = requests.get('https://data.ct.gov/resource/htz8-fxbk.json');
#resp = requests.get('https://data.ct.gov/resource/nevh-exab.json')
#.loads() method turns the JSON into a python object
result = json.loads(resp.content)

for entry in result:
    print(entry)
    print("\n")


#Class that holds the values from the parsed JSON will be here
#Does it make sense to convert it into an object or should I keep it as a JSON in result?

RadiusLocator.GeoLocation()