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
    users = csv.reader(open('users',"r"), delimiter=",")
    userlist = []
    for row in users:
        userlist.append(row)
    kill = False
    while kill == False:
        user, found = ("",[])
        user = input("What user would you like to find?")
        for row in userlist:
            if row[0] == user:
                found.append(row)
        if len(found) == 1:
            print (f"found user {found[0][0]} email :{found[0][2]} birthdate:{found[0][3]}")
            x = input("Would you like to try to find a user again? \n                              yes/no \n")
            kill =False if x== "yes" else True
        elif len(found) > 1: print('there are multiple users with this name')
        else: 
            x = input(f"User:{user} was not found, would you like to try to find a user again? \n yes/no")
            kill =False if x== "yes" else True

def updateUser():
    pass

def deleteUser():
    users = csv.reader(open('users',"r"), delimiter=",",lineterminator="\n")
    userList = []
    for row in users:
        userList.append(row)
    user = input("What user would you like to delete? \n")
    for idx, row in enumerate(userList):    
        if user == row[0]:
            deleteVerify = input(f"user found, would you like to delete {row[0]}")
            if deleteVerify == "yes":
                userList.pop(idx)
                userdel = csv.writer(open (f'users', 'w'), delimiter=",", lineterminator='\n')
                for user in userList:
                    userdel.writerow([user[0],user[1],user[2],user[3],user[4]])
                print('user succesfully deleted')
            else:print("sounds good, we will bring you back to the menu")
    
kill = False
while kill == False:
    options = input("What would you like to do?")
    if options == "create":createUser()
    elif options == "find":findUser()
    elif options == "delete":deleteUser()
    elif options == "end": kill = True
    else: print("That is not an option, you can either, create, find, update, delete a user, or end")