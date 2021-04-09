from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT
from security import authenticateuser, identity
from Resources.users import modifyusers
from Resources.items import Item, postItem
from Resources.stores import Stores, AddStore
from db import db

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thisismydb.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/storenew'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = "london"
jwt = JWT(app, authenticateuser, identity)


class Items(Resource):
    def get(self):
        print("I am in get all items")
        return None


api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<int:itemid>')
api.add_resource(postItem, '/item')
api.add_resource(modifyusers, '/users')
api.add_resource(Stores, '/store/<int:storeId>')
api.add_resource(AddStore, '/store')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=3500, debug=True)
