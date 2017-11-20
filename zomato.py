# -*- coding: utf-8 -*-

import requests,json

class Zomato():

    def __init__(self, token):

        self.token = token
        self.base_url = "https://developers.zomato.com/api/v2.1/"

    def get_City(self, lat, lon):
        
        data = requests.get(self.base_url+"geocode?lat="+lat+"&lon="+lon, headers={"user-key":self.token})
        return data

    def get_nearby_location(self,location_obj,money_count):
        
        recommodation_data = []
        tmp_rec = {}
            ##ask to the zomato
        payload = {'user-key': '{}'.format(self.token)}

        restaurant_data = requests.get("https://developers.zomato.com/api/v2.1/geocode?lat={}&lon={}".format(location_obj['latitude'],location_obj['longitude']),headers=payload)      
        tmp_data =  json.loads(restaurant_data.content)
        
        print(tmp_data)
        for i in tmp_data["nearby_restaurants"]:
            control_price = int(i['restaurant']['average_cost_for_two'])

            if control_price/2 <= money_count:
                tmp_rec['address'] =  i['restaurant']['location']['address']
                tmp_rec['name'] = i['restaurant']['name']
                tmp_rec['req_money'] = control_price
            
            recommodation_data.append(tmp_rec)
        return recommodation_data

