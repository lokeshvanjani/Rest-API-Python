import sqlite3
from flask_restful import Resource, reqparse
from module6code.MyModels.user import UsersModel
from flask_jwt import jwt_required


class modifyusers(Resource):
    @jwt_required()
    def post(self):
        myparser = reqparse.RequestParser()
        myparser.add_argument('username', type=str, required=True, help='Username is required')
        myparser.add_argument('password', type=str, required=True, help='Password is required')
        mydata = myparser.parse_args()

        adduserobject = UsersModel(None, mydata['username'], mydata['password'])
        returndata = adduserobject.insertuser()

        if returndata == 0:
            return {"message": "User Inserted Successfully"}, 201
        elif returndata == -1:
            return {"message": "User already exist"}, 400
        else:
            return {"message": "Internal server error"}, 500

    def get(self):
        myobject = UsersModel(None, None, None)
        mydata = myobject.getAllUsers()

        myreturndata_main = []
        for i in mydata:
            myreturndata = {}
            myreturndata['id'] = i.id
            myreturndata['username'] = i.username
            myreturndata['password'] = i.password
            myreturndata_main.append(myreturndata)
        return {"items": myreturndata_main}, 200
