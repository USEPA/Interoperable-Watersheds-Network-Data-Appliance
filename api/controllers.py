from flask_restplus import Resource, marshal_with
import serializers

class GreeterController(Resource):
    @marshal_with(serializers.greeter)
    def get(self):
        return {'name' :'Fred', 'message' : 'Hellooooooo'}