from flask import Flask, request, url_for
import json

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    sensor = request.form['sensor']
    request_json = json.loads(sensor)
    print request_json

    sensor_values = request_json['values']
    if sum(sensor_values) > 6.0:
        return 'run'
    else:
        return 'walk'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
