from module6code.db import db

class UsersModel(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, userid, username, password):
        self.id = userid
        self.username = username
        self.password = password

    def fetchuserbyname(self):
        return self.query.filter_by(username=self.username).first()

    def fetchuserbyid(self):
        return self.query.filter_by(id = self.id).first()

    def insertuser(self):
        try:
            userexist = self.query.filter_by(username=self.username).first()
            if userexist:
                return -1
            db.session.add(self)
            db.session.commit()
            return 0
        except Exception as e:
            print("Exception occured in inserting user")
            print(e)
            return -2

    def getAllUsers(self):
        return self.query.all()