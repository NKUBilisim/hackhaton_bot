import requests

class Zomato():

    def __init__(self, token):

        self.token = token
        self.base_url = "https://developers.zomato.com/api/v2.1/"

    def get_City(self, lat, lon):

        data = requests.get(self.base_url+"geocode?lat="+lat+"&lon="+lon, headers={"user-key":self.token})
        return data