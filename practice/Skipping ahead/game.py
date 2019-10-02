print("you are a car")
death = False
car_distance = 0
curr_action = ""
while death == False:
    action = input()
    if action == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif action == "start":
        car_distance += 1
        print(f'the car is going and has gone {car_distance}')
        curr_action = action
    elif action == "stop":
        print(f"the car has stopped and has gone {car_distance}")
        curr_action = action
    elif action == "quit":
        print(f"the car has gone {car_distance} before you killed it's dream")
        death = True
    else:
        print("error: incorrect answer type help for help if you're a bonobo")
        if curr_action == "start":
            car_distance +=1
            print(f'the car is still on, so you have gone 1 more distance, leaving you at {car_distance} distance')
#A game that works, not very good, but it works