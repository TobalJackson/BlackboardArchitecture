#!/usr/bin/env python3

"""
experts = Chef, Hunter, Lumberjack, Blacksmith, Survivalist, Doctor, Driver

Skills = cooking(food), hunting(animal), chopping(wood), repair(tool), locate(natural_resource), heal(person), drive(caravan)


Start the script:
    description of situation
        (in the woods/desert/etc. 
    State some need:
        Hunger
        sleep
        water
    Experts show their utility verbally

    Arbiter selects experts for tasks

    Experts report success of tasks

    Show status change

"""
import random
from Expert import Expert


#task: Need Food
#   Chef: expresses insistence('I can cook food') but needs('Ingredients', 'Fire')#   LumberJack: expresses insistence('I can get wood')
#   Hunter: expresses insistence('I can hunt meat')
#   Survivalist: expresses insistence('I can get fresh water/veggies')

blackboard = {"inventory":[], "needs":[]}



print("\nThe travelers have taken a wrong turn and have ended up lost in The Great Forest of Ashwood.  At first they're focused on just finding their way.")
chef = Expert("Chef", blackboard, cooking=0.99)
hunter = Expert("Elmer", blackboard, hunting=0.99)
lumberjack = Expert("Paul", blackboard, chopping=0.99)
survivalist = Expert("Bear", blackboard, survivalism=0.99)

experts = [chef, hunter, lumberjack, survivalist]
for expert in experts:
    print("{}'s insistence: {:1.3f}".format(expert.name, expert.getInsistence()))

print("\nIt has been nearly 8 hours since they've seen any sign of the designated trail, and they're beginning to get hungry.")

blackboard["needs"].append("food")

lastExpert = None
lastInsistence = None

while "food" in blackboard["needs"] and "food" not in blackboard["inventory"]:
    maxInsistence = 0
    bestExpert = None
    for expert in experts:
        if expert == lastExpert:
            continue
        insistence = expert.getInsistence()
        print("\t{}'s insistence: {:1.3f}".format(expert.name, insistence))
        if insistence > maxInsistence:
            maxInsistence = insistence
            bestExpert = expert
    
    if bestExpert is not None:
        print("{} has something to contribute to the group!".format(bestExpert.name))
        bestExpert.run(blackboard)
        lastExpert = bestExpert
    for item in blackboard["inventory"]:
        if item in blackboard["needs"]:
            blackboard["needs"].remove(item)
    print("\n\tInventory: {}\n\tNeeds: {}".format(blackboard["inventory"], blackboard["needs"]))

