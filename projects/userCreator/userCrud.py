import csv
import uuid
class userCreator():
    def __init__(self, userdata):
        self.username = userdata[0]
        self.password = userdata[1]
        self.email = userdata[2]
        self.birthdate = userdata[3]
        self.uuid = userdata[4]
        

def createUser():
    user = input("type your username")
    password = input("type your password")
    email = input("type your email")
    bday = input("type your bday")
    user_id = uuid.uuid4()
    newUser = userCreator([user,password,email,bday,user_id])
    users = csv.writer(open (f'users', 'a'), delimiter=",", lineterminator='\n')
    users.writerow([newUser.username,newUser.password,newUser.email,newUser.birthdate,newUser.uuid])
def findUser():
    pass
def updateUser():
    pass
def deleteUser():
    pass
createUser()