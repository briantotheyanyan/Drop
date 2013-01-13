<<<<<<< HEAD
from pymongo import Connection
import math
import unicodedata
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
    allMessages = Messages.find()
    longitude = (eval(str(longitude)))
    latitude = (eval(str(latitude)))
    messagesinRange = []
    for current in allMessages:
        x=eval(str(current['longitude']))
        y=eval(str(current['latitude']))
        if ((longitude-x)*(longitude-x))+((latitude-y)*(latitude-y)) <= 1:
            if messagesinRange == None:
                messagesinRange = [str(current['text'].encode('ascii','ignore'))]
            else:
                messagesinRange.append(str(current['text'].encode('ascii','ignore')))
    return messagesinRange
if __name__ == '__main__':
    Messages.drop()
=======
from pymongo import Connection
import math
import unicodedata
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
    allMessages = Messages.find()
    messagesinRange = []
    for current in allMessages:
        if ((current['longitude']-longitude) * (current['longitude']-longitude) + (current['latitude']-latitude)*(current['latitude']-latitude)) <= 1:
            if messagesinRange == None:
                messagesinRange = [current['text']]
            else:
                messagesinRange.append(current['text'])
    return messagesinRange
>>>>>>> 4f1628c40e1bdf5e3ac7f973ead159524b12e97a
