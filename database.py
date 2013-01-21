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

def writeMessage(text,longitude,latitude,username):
	Messages.insert({'text':text,'longitude':longitude,'latitude':latitude,'username':username, 'date': date,'time': time})

def returnAllMessages():
    allMessages = Messages.find()
    MessageList = []
    for current in allMessages:
        x = [current['longitude'],current['latitude'], "" + str(current['username'].encode('ascii','ignore'))]
        
        if MessageList == None:
            MessageList = [x]
        else:
            MessageList.append(x)
            
    
    return MessageList

def returnMessagesinRange(longitude,latitude):
    allMessages = Messages.find()
    longitude = (eval(str(longitude)))
    latitude = (eval(str(latitude)))
    messagesinRange = []
    for current in allMessages:
        y=eval(str(current['longitude']))
        x=eval(str(current['latitude']))
        if ((longitude-x)*(longitude-x))+((latitude-y)*(latitude-y)) <= (0.00089992800576*0.00089992800576):
            if messagesinRange == None:
                messagesinRange = [str(current['text'].encode('ascii','ignore'))]
            else:
                messagesinRange.append(str(current['text'].encode('ascii','ignore')))
    return messagesinRange
if __name__ == '__main__':
    print returnAllMessages()
    #pass
    #Messages.drop()
    #Accounts.drop()
