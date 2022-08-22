from flask import Flask
from flask_restful import Api, Resource
import csv
from appl_per_user import appl_per_user
from users_per_appl import users_per_appl

app = Flask(__name__)
api = Api(app)

class getApplicationPerUser(Resource):
    def get(self, userId):
        try:
            userId = int(userId)
            #return {"userId" : userId}
            return appl_per_user(userId)
        except:
            # Need to be expanded? send back error code
            return "Error : Wrong type for userID"

class getApplicationPerJob(Resource):
    def get(self, jobId):
        try:
            jobId = int(jobId)
            #return {"jobId" : jobId}
            return users_per_appl(jobId)
        except:
            return "Error : Wrong type for jobId"        

# link the endpoints to the classes created to handle them
api.add_resource(getApplicationPerUser, "/getApplicationPerUser/<string:userId>")
api.add_resource(getApplicationPerJob, "/getApplicationPerJob/<string:jobId>")


if __name__ == "__main__":
    app.run(debug=True)