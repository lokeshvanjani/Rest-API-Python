from module6code.db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    __table_args__ = {'extend_existing': True}
    storeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('FindItemByID', lazy='dynamic')

    def __init__(self, storeId, name):
        self.storeId = storeId
        self.name = name

    def fetchstorebyid(self):
        return self.query.filter_by(storeId=self.storeId).first()

    def fetchstorebyname(self):
        return self.query.filter_by(name=self.name).first()

    def returnjson(self):
        return {"storeId": self.storeId, "name": self.name, "items": [i.returnjson() for i in self.items.all()]}

    def updatestore(self):
        try:
            mydata = self.fetchstorebyid()
            if mydata:
                mydata.name = self.name
                db.session.commit()
                return 0
            return -1
        except Exception as e:
            print("Exception occurred while updating store")
            print(e)
            return -2

    def deletestore(self):
        try:
            mydata = self.fetchstorebyid()
            if mydata:
                db.session.delete(mydata)
                db.session.commit()
                return 0
            return -1

        except Exception as e:
            print("Exception occurred while deleting store")
            print(str(e.__dict__['orig']))
            print(e.__dict__['orig'] == (1048, "Column 'storeid' cannot be null"))
            db.session.rollback()
            return -2

    def insertstore(self):
        try:
            mydata = self.fetchstorebyname()
            if mydata:
                return -1
            db.session.add(self)
            db.session.commit()
            return 0
        except Exception as e:
            print("Exception occurred while inserting store")
            print(e)
            return -2
