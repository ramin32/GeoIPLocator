from flask import Flask, request, render_template
import pygeoip
from datetime import datetime

app = Flask(__name__)
geoip = pygeoip.GeoIP('GeoLiteCity.dat')

@app.route("/")
def hello():
    ip = str(request.remote_addr)
    record = geoip.record_by_addr(ip)

    return render_template('index.html', 
                           ip=ip,
                           record=record,
                           year=datetime.now().year)


if __name__ == "__main__":
    app.debug = True
    app.run()
