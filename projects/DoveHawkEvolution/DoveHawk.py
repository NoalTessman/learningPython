import uuid
import random
birdAmount = 25
rounds = 15
birdPool = []
#initial variables

class DoveCreator:
    bird_id = 0
    birdcount = 0
    species = "dove"
    food = 0
    dead = False
    def __init__(self,bird_uuid):
        self.bird_uuid = bird_uuid
        self.bird_id= DoveCreator.birdcount
        DoveCreator.birdcount +=1
        self.species = "dove"
        self.food = 0
        self.dead = False
#Creates a Dove
#Having troubles building birds with consequtive ids so each of the little guys gets uuid4.
#Eventually make a birdcreator instead of a hawk and dove creator
class hawkCreator:
    species = "hawk"
    food = 0
#creates a Hawk, not used yet

def createBirds():
    for x in range(birdAmount):
        birdPool.append(DoveCreator(uuid.uuid4()))
#adds birds to birdPool, quick way to get a disease

octagonPool = []
octagonAmount = 25
octagonFoodcount = 2
#fight round initial variables

class createOctagon():
    room = 0
    bird1 = {}
    bird2 = {}
    def __init__(self):
        room = 0
        bird1 = 0
        bird2 = 0
    #Creates octagon Object

def createOctagons():
    for x in range(octagonAmount):
        room = createOctagon()
        room.room = x
        room.bird1 =0
        room.bird2 =0
        octagonPool.append(room)
#creates octogans
def emptyBirdPool(birdpool):
    del birdPool[x]

deadBirds = []
resultsPool = []
def octagonSelect(birdPool, octagonPool):
   for x in range(len(birdPool)):
        randomRoom = random.randint(0,len(octagonPool)-1)
        if octagonPool[randomRoom].bird1 == 0:
            octagonPool[randomRoom].bird1 = birdPool[x]
        elif octagonPool[randomRoom].bird2 == 0:
            octagonPool[randomRoom].bird2 = birdPool[x]
        else:
            birdPool[x].dead = True
            deadBirds.append(birdPool[x])

def fightRound(birdPool, octagonPool):
    for x in range(len(octagonPool)):
        if octagonPool[x].bird1 != 0:
            if octagonPool[x].bird2 !=0:
                octagonPool[x].bird1.food, octagonPool[x].bird2.food = 1,1
                birdPool.extend((octagonPool[x].bird1,octagonPool[x].bird2))
            else: 
                octagonPool[x].bird1.food = 2
                birdPool.append(octagonPool[x].bird1)
    
def survival(birdPool):
    for x in birdPool:
        use = "less"

#octagonSelect(birdPool,octagonPool)
def wholeEvent():
    createBirds()
    createOctagons()
    octagonSelect(birdPool,octagonPool)
    fightRound(birdPool,octagonPool)
    emptyBirdPool(birdPool)
    survival(birdPool)
wholeEvent()
#Bird Testing
for x in birdPool:
        print(x.__dict__)
#Octagon Testing
#for x in octagonPool:
#    print(x.__dict__)