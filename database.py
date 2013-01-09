from pymongo import Connection
Connection = Connection('mongo.stuycs.org')
db=Connection.admin
res=db.authenticate('ml7','ml7')
Accounts= db.Accounts
Messages = db.Messages

def createAccount(username,password,birthday):
    if Accounts.find({'usernames':username}).count() == 0:
        Accounts.insert({'usernames':username,'birthday':birthday,'passwords':password})
        return True
    else:
        return False
def verifyAccount(username,password):
    if Accounts.find({'usernames':username}).count() != 0:
        return True
    else:
        return False

def writeMessage(text,longitude,latitude):
    Messages.insert({'text':text,'longitude':longitude,'latitude':latitude})

def returnMessagesinRange(longitude,latitude):
    #Ok, so a degree of longitude and latitude is about 111 km, if we want to make it within 100m, we need to use pythag theorem, and convert the distances of the longitude and latitude into it. So yah... :P. Shouldn't be too difficult.
    pass
