import requests,json

class Zomato():

    def __init__(self, token):

        self.token = token
        self.base_url = "https://developers.zomato.com/api/v2.1/"

    def get_City(self, lat, lon):
        
        data = requests.get(self.base_url+"geocode?lat="+lat+"&lon="+lon, headers={"user-key":self.token})
        return data

    def get_nearby_location(self,location_addr):
        data = requests.get("http://localhost:5000/addr_to_co?{}".format(location_addr))
        coor_data = json.loads(data.content)
        print(coor_data)
        try:
            ##ask to the zomato
            payload = {'user-key': '{}'.format(self.token)}

            restaurant_data = requests.get("https://developers.zomato.com/api/v2.1/geocode?lat{}&lon={}".format(coor_data['lat'],coor_data['long']),headers=payload)      
            tmp_data =  json.loads(restaurant_data.content)


            return tmp_data["nearby_restaurants"]["id"]
        except:
            ###exception handling on ask to the zomato 
            pass ##rabbitmq


obj = Zomato("ba778a4b6afff374876684ada9ddeac1")
print(obj.get_nearby_location("Istanbul")) 