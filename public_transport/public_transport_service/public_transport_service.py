from flask import Flask,render_template,request
     
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_geo():
    
        start_ln = request.args.get("start_ln")
        start_lon = request.args.get("start_lon")

        finish_ln = request.args.get("finish_ln")
        finish_lon = request.args.get("finis_lon")
        
        return "http://localhost:5000/transport?start_ln=28.91846180&start_lon=41.01662773&finish_ln=28.93090725&finish_lon=41.00781966"


@app.route("/transport",methods=['GET'])
def get_public_transport_data():

    start_ln = request.args.get("start_ln")
    start_lon = request.args.get("start_lon")

    finish_ln = request.args.get("finish_ln")
    finish_lon = request.args.get("finis_lon")

    return render_template("result.html",data=({'sLn':start_ln,'sLon':start_lon,'fLn':finish_ln,'fLon':finish_lon}))




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)