from flask import Flask
from flask_restful import Resource, Api
import time

app = Flask(__name__)
api = Api(app)

class GetDetail(Resource):
    def get(self):
        # time.sleep(6)
        return "Python API"

api.add_resource(GetDetail, '/getname')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8001')
