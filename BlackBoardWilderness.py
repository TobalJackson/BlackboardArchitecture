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

blackboard = {"tasks":{}, "inventory":[], "needs":[]}



situation = "The travelers have taken a wrong turn and have ended up lost in The Great Forest of Ashwood. It has been nearly 8 hours since they've seen any sign of the designated trail, and they're beginning to get hungry." 

chef = Expert("Chef",cooking=0.99)
hunter = Expert("Elmer", hunting=0.99)
lumberjack = Expert("Paul", chopping=0.99)
survivalist = Expert("Bear", survivalism=0.99)

