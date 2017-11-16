from flask import Flask, jsonify,request
import requests,json
app = Flask(__name__)


@app.route('/addr_to_co', methods=['GET'])
def get_tasks():
    
        addr_location = request.args.get("my_addr")
        data = requests.get("http://maps.google.com/maps/api/geocode/json?address={}".format(addr_location))
        tmp_data = json.loads(data.content)
        try:
            return jsonify(lat=tmp_data["results"][0]["geometry"]["bounds"]["northeast"]["lat"],long=tmp_data["results"][0]["geometry"]["bounds"]["northeast"]["lng"])
        except:
            return jsonify(status=False)
if __name__ == '__main__':
    app.run(debug=True)



