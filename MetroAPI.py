import requests

class MetroAPI:
    def __init__(self):
        self.base_url = "https://api.metro.net/agencies/lametro/"

    def get_all_vehicle_locations(self):
        vehicle_url  = self.base_url + "vehicles/" 
        response = requests.get(vehicle_url)
        return response.json()["items"]

    #example of complete url
    #http://api.metro.net/agencies/lametro/routes/704/vehicles/
    def get_vehicle_location(self, routeNumber="704"):
        vehicle_url = self.base_url + "routes/" + routeNumber + "/vehicles/"
        response = requests.get(vehicle_url)
        return [] if len(response.json()["items"]) == 0 else  response.json()["items"][0]

