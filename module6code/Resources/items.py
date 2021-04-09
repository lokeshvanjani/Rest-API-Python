from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from module6code.MyModels.item import FindItemByID

class Item(Resource):

    @jwt_required()
    def get(self, itemid):
        myobject = FindItemByID(itemid, None, None, None)
        mydata = myobject.finditem_byid()
        if mydata:
            return {"result": mydata.returnjson()}, 200
        return {"message": "Item not found"}, 404

    @jwt_required()
    def delete(self, itemid):
        myobject = FindItemByID(itemid, None, None, None)
        myitemfound = myobject.deleteitem()
        if myitemfound == 0:
            return {"message": "Item deleted successfully"}, 200
        elif myitemfound == -1:
            return {"message": "Item not found"}, 404
        return {"message": "Internal server error"}, 500

    @jwt_required()
    def put(self, itemid):
        myparser = reqparse.RequestParser()
        myparser.add_argument('name', type=str, required=True, help="Name is required")
        myparser.add_argument('price', type=float, required=True, help="Price is required")
        myparser.add_argument('storeId', type=int, required=True, help="Store ID is required")
        datapassed = myparser.parse_args()

        myupdateitem = FindItemByID(itemid, datapassed['name'], datapassed['price'], datapassed['storeId'])
        returnvalue = myupdateitem.updateitem()
        if returnvalue == 0:
            return datapassed, 200
        elif returnvalue == -1:
            return {"message": "Item not found"}, 404
        else:
            return {"message": "Not able to delete, internal server error"}, 500


class postItem(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="Name is required")
        parser.add_argument('price', type=float, required=True, help="Price is required")
        parser.add_argument('storeId', type=int, required=True, help="Store ID is required")
        mydata = parser.parse_args()

        myobject = FindItemByID(None, mydata['name'], mydata['price'], mydata['storeId'])
        returnedselectdata = myobject.insertitem()

        if returnedselectdata == 0:
            return mydata, 201
        elif returnedselectdata == -1:
            return {"message": "Item already exist"}, 400
        else:
            return {"message": "Internal server error"}, 500
