from flask import Flask,jsonify,request
api = Flask(__name__)


@api.route("/addr_to_coo/")
def addr_to_coo():
    if request.method == 'POST':
        addr_location = request.args.post('my_addr', '')
        try:
            data = request.get("http://maps.google.com/maps/api/geocode/json?address={}".format(addr_location))
            return data.json
        except:    
            return  jsonify(status=False)




app.run()




