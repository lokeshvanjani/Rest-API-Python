from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from module6code.MyModels.store import StoreModel

class Stores(Resource):
    @jwt_required()
    def get(self, storeId):
        myobject = StoreModel(storeId, None)
        mydata = myobject.fetchstorebyid()
        if mydata:
            return {"result": mydata.returnjson()}, 200
        return {"message": "Store not found"}, 404

    @jwt_required()
    def put(self, storeId):
        myparser = reqparse.RequestParser()
        myparser.add_argument('name', type=str, required=True, help='Name is required')
        datapassed = myparser.parse_args()

        myobject = StoreModel(storeId, datapassed['name'])
        returndata = myobject.updatestore()
        if returndata == 0:
            return datapassed, 200
        elif returndata == -1:
            return {"message": "Store not found"}, 404
        else:
            return {"message": "Internal server error"}, 500

    @jwt_required()
    def delete(self, storeId):
        myobject = StoreModel(storeId, None)
        returndata = myobject.deletestore()
        if returndata == 0:
            return {"message": "Store deleted successfully"}, 200
        elif returndata == -1:
            return {"message": "Store not found"}, 404
        else:
            return {"message": "Internal server error"}, 500

class AddStore(Resource):
    @jwt_required()
    def post(self):
        myparser = reqparse.RequestParser()
        myparser.add_argument('name', required=True, type=str, help='Name is required')
        datapassed = myparser.parse_args()

        myobject = StoreModel(None, datapassed['name'])
        returneddata = myobject.insertstore()
        if returneddata == 0:
            return {"message": "Store inserted successfully"}, 201
        elif returneddata == -1:
            return {"message": "Store already exist"}, 400
        else:
            return {"message": "Internal server error"}, 500
