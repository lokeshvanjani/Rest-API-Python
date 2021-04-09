from MyModels.user import UsersModel


def authenticateuser(username, password):
    myobject = UsersModel(None, username, password)
    mydata = myobject.fetchuserbyname()
    if mydata and mydata.password == password:
        return mydata
    else:
        return None


def identity(payload):
    myuserid = payload['identity']
    myobject = UsersModel(myuserid, None, None)
    mydata = myobject.fetchuserbyid()
    return mydata

