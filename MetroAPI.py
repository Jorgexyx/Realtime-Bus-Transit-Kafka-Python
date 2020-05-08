import requests

class MetroAPI:
    def __init__(self):
        self.base_url = "https://api.metro.net/agencies/lametro/"

    def get_route_predictions(self, busNumber=6033):
        predictions_url = self.base_url + "vehicles/" 
        response = requests.get(predictions_url)
        return response.content

