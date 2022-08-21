from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class getApplicationPerUser(Resource):
    def get(self, userId):
        try:
            userId = int(userId)
            return {"userId" : userId}
        except:
            return "Error : Wrong type for userID"

class getApplicationPerJob(Resource):
    def get(self, jobId):
        try:
            jobId = int(jobId)
            return {"jobId" : jobId}
        except:
            return "Error : Wrong type for jobId"        

api.add_resource(getApplicationPerUser, "/getApplicationPerUser/<string:userId>")
api.add_resource(getApplicationPerJob, "/getApplicationPerJob/<string:jobId>")


if __name__ == "__main__":
    app.run(debug=True)