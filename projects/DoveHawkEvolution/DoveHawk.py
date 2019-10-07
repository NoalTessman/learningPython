import uuid
import random
import csv


birdAmount = 2
rounds = 15
birdPool = []
octagonPool = []
octagonAmount = 25
octagonFoodcount = 2
#Initial Variables



#Test function
def birdTest():
    for x in birdPool:
        print(x.__dict__)
def deadBirdTest():
    for x in deadBirds:
        print(x.__dict__)
def birdCount():
    print(len(birdPool))




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
#Having troubles building birds with consequtive ids so each oemptyBirdPool(birdPool) the little guys gets uuid4.
#Eventually make a birdcreator instead of a hawk and dove creaemptyBirdPool(birdPool)or
class hawkCreator:
    species = "hawk"
    food = 0
#creates a Hawk, not used yet

def createBirds():
    for x in range(birdAmount):
        birdPool.append(DoveCreator(uuid.uuid4()))
#adds birds to birdPool, quick way to get a disease
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
def emptyBirdPool(birdPool):
    birdPool.clear()
#deletes birdPool to be populated with returning octagon birds
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

def graphAdder(Generation):
    wtr.writerow([Generation,len(birdPool)])

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
        if x.food == 2:
            birdPool.append(DoveCreator(uuid.uuid4()))
            


#octagonSelect(birdPool,octagonPool)
def initialize():
    createBirds()
    createOctagons()
def wholeEvent():
    octagonSelect(birdPool,octagonPool)
    emptyBirdPool(birdPool)
    fightRound(birdPool,octagonPool)
    graphAdder(Generation)
    survival(birdPool)


#Output result to graph
wtr = csv.writer(open (f' {birdAmount}Birds {octagonAmount}Octagons 2 food Doves Only.csv', 'w'), delimiter=',', lineterminator='\n')
wtr.writerow(["bird Amount", "Generation"])
#Creates csv with two lines

#Running the program
initialize()
for i in range(10):
    Generation = i + 1
    wholeEvent()
    birdCount()