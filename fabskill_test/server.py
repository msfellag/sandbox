from flask import Flask
from flask_restful import Api, Resource


from appl_per_user import applications_per_user
from users_per_appl import users_per_application

app = Flask(__name__)
api = Api(app)

class getApplicationPerUser(Resource):
    def get(self, userId):
        # Test if the userID is convertible to an integer
        # if not send back a 406 error
        try:
            int(userId)
        except:
            return "Error : Wrong type for userID", 406
        return applications_per_user(userId)

class getApplicationPerJob(Resource):
    def get(self, jobId):
        # Test if the jobID value is convertible to an integer
        try:
            int(jobId)
        except:
            return "Error : Wrong type for jobId", 406

        return users_per_application(jobId)     

# link the endpoints to the classes created to handle them
api.add_resource(getApplicationPerUser, "/getApplicationPerUser/<string:userId>")
api.add_resource(getApplicationPerJob, "/getApplicationPerJob/<string:jobId>")


if __name__ == "__main__":
    app.run(debug=True)