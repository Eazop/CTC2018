import json
class Location:
    location = None
    address = ""
    name = ""
    street = ""
    town = ""
    zipCode = ""
    service = ""
    phoneNumber = ""

    def init(self, name, phone, location, address, town, zipCode, service):
        self.location = location
        self.address = address
        self.name = name
        self.town = town
        self.zipCode = zipCode
        self.service = service
        self.phoneNumber = phone

    #def distanceFrom(latitude, longitude):
        #logic goes here