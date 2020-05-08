import requests

class MetroAPI:
    def __init__(self):
        self.base_url = "https://api.metro.net/agencies/lametro/"

    #just return first vehicle
    #todo impement
    def get_random_vehicle_locations(self, busNumber=6033):
        vehicle_url  = self.base_url + "vehicles/" 
        response = requests.get(vehicle_url)
        return response.content

    #example of complete url
    #http://api.metro.net/agencies/lametro/routes/704/vehicles/
    def get_vehicle_location(self, routeNumber=704):
        vehicle_url = self.base_url + "routes/" + str(routeNumber) + "/vehicles/"
        response = requests.get(vehicle_url)
        return response.json()["items"][0]

