class Location:
    latitude = 0.0
    longitude = 0.0
    title = ""
    street = ""
    town = ""
    zipCode = ""
    service = ""

    def init(self, latitude, longitude, title, street, town, zipCode, service):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.street = street
        self.town = town
        self.zipCode = zipCode
        self.service = service

    def distanceFrom(latitude, longitude):
        #logic goes here


        