from module6code.db import db

class FindItemByID(db.Model):
    __tablename__ = 'items'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    storeId = db.Column(db.Integer, db.ForeignKey('stores.storeId'), nullable=False)

    def __init__(self, itemid, name, price, storeId):
        self.id = itemid
        self.name = name
        self.price = price
        self.storeId = storeId

    def returnjson(self):
        return {"name": self.name, "price": self.price, "storeId": self.storeId}

    def finditem_byid(self):
        return self.query.filter_by(id=self.id).first()
        #db.session.query(self).filter(id=self.id).first()

    def finditem_byname(self):
        return self.query.filter_by(name=self.name).first()
        #db.session.query(self).filter(name=self.name).first()

    def deleteitem(self):
        try:
            myobject = self.query.filter_by(id=self.id).first()
            if myobject:
                db.session.delete(myobject)
                db.session.commit()
                return 0
            return -1
        except Exception as e:
            print(e)
            return -2

    def insertitem(self):
        try:
            myobject = self.query.filter_by(name=self.name).first()
            if myobject:
                return -1
            db.session.add(self)
            db.session.commit()
            return 0
        except Exception as e:
            print(e)
            return -2

    def updateitem(self):
        try:
            myobject = self.query.filter_by(id=self.id).first()
            if myobject:
                myobject.name = self.name
                myobject.price = self.price
                myobject.storeId = self.storeId
                db.session.commit()
                return 0
            return -1
        except Exception as e:
            print(e)
            return -2
