#!/usr/bin/env python3

import random
import operator

class Expert:
    def __init__(self, name, blackboard, hunger=50, health=50, cooking=0.25, hunting=0.25, chopping=0.25, survivalism=0.25, variability=0.1):
        self.blackboard = blackboard

        self.hunger = hunger 
        self.health = health 
        self.name = name

        self.cooking = cooking - (random.random() * variability)
        self.hunting = hunting  - (random.random() * variability)
        self.chopping = chopping - (random.random() * variability)
        self.survivalism = survivalism  - (random.random() * variability)

        self.skills = {"cooking":self.cooking, "hunting":self.hunting, "chopping":self.chopping, "survivalism":self.survivalism}
        self.sortedSkills = sorted(self.skills.items(), key=operator.itemgetter(1), reverse=True)

        #self.inventory = blackboard["inventory"]
        self.tasks = []

    def cook(self, food_difficulty=1.0):
        if "food" in self.blackboard["inventory"]:
            print("We already have food!")
            return
        if "meat" in self.blackboard["inventory"] and "water" in self.blackboard["inventory"] and "fire" in self.blackboard["inventory"]:
            difficulty = self.cooking / food_difficulty
            result = random.random() < difficulty
            if (result):
                print("I have successuflly cooked the food. Enjoy!")
                self.blackboard["inventory"].append("food")
                self.blackboard["needs"].remove("food")
            else:
                print("I screwed this dish up.  We could eat it at the risk of...Dysentery")
                self.blackboard["inventory"].remove("meat")
                self.blackboard["inventory"].remove("water")
                self.blackboard["inventory"].remove("fire")
        else:
            if "meat" not in self.blackboard["inventory"]:
                self.blackboard["needs"].append("meat")
                print("Chef: We need Meat!")
            if "water" not in self.blackboard["inventory"]:
                self.blackboard["needs"].append("water")
                print("Chef: We need Water!")
            if "fire" not in self.blackboard["inventory"]:
                self.blackboard["needs"].append("fire")
                print("Chef: We need Fire!")

    def hunt(self, animal_difficulty=1.0):
        inventory = self.blackboard["inventory"]
        needs = self.blackboard["needs"]
        difficulty = self.hunting / animal_difficulty
        result = random.random() < difficulty
        if "meat" in inventory:
            print("{}: We already have meat!".format(self.name))
            if "meat" in needs:
                needs.remove("meat")
            return
        elif (result):
            print("{}:I have successfully hunted for meat!  Let's cook it!".format(self.name))
            inventory.append("meat")
            needs.remove("meat")
        else:
            print("{}: I have failed this hunting mission.  Shall we eat our boots?".format(self.name))

    def chop(self, wood_difficulty=1.0):
        difficulty = self.chopping  / wood_difficulty
        result = random.random() < difficulty
        if "wood" in self.blackboard["inventory"]:
            print("{}: We already have some wood!".format(self.name))
            return
        elif (result):
            print("{}: I have chopped the wood.  Lets make something with this fine wood".format(self.name))
            self.blackboard["inventory"].append("wood")
            self.blackboard["needs"].remove("wood")
        else:
            print("{}: I have failed miserably! We must try again to get wood.".format(self.name))
        return result

    def survival(self, resource_difficulty=1.0):
        difficulty = self.survivalism  / resource_difficulty
        result = random.random() < difficulty
        if "water" in self.blackboard["inventory"] and "fire" in self.blackboard["inventory"]:
            print("{}: We already have water and Fire.  Better drink my own piss...".format(self.name))
        elif "water" in self.blackboard["needs"]:
            if (result):
                print("{}: I have found some water! Let's enjoy it while it lasts..".format(self.name))
                self.blackboard["inventory"].append("water")
                self.blackboard["needs"].remove("water")
            else:
                print("{}: I've failed to find any water.  We can all drink my piss...".format(self.name))
        elif "fire" in self.blackboard["needs"]:
            if "wood" in self.blackboard["inventory"]:
                if (result):
                    print("{}: I have made a fire! Let us bask in its warmth and/or use it to cook!".format(self.name))
                    self.blackboard["inventory"].append("fire")
                    self.blackboard["needs"].remove("fire")
                    self.blackboard["inventory"].remove("wood")
                else:
                    print("{}: I have screwed up making the fire! We need more wood...".format(self.name))
                    self.blackboard["inventory"].remove("wood")
            else:
                print("{}: We need wood to make a fire!".format(self.name))
                self.blackboard["needs"].append("wood")
            


    def run(self, blackboard):
        myStrength = self.sortedSkills[0][0]
        if myStrength == "cooking":
            self.cook()
        if myStrength == "chopping":
            self.chop()
        if myStrength == "hunting":
            self.hunt()
        if myStrength == "survivalism":
            self.survival()



    def getInsistence(self):
        Insistences = [0]
        if "water" in self.blackboard["needs"]:
            Insistences.append(self.survivalism)
        if "fire" in self.blackboard["needs"]:
            insistence = self.survivalism
            if "wood" not in self.blackboard["inventory"]:
                insistence = insistence - 0.25
            Insistences.append(insistence)
        if "meat" in self.blackboard["needs"]:
            Insistences.append(self.hunting)
        if "food" in self.blackboard["needs"]:
            insistence = self.cooking
            if "water" not in self.blackboard["inventory"]:
                insistence = insistence - 0.25
            if "meat" not in self.blackboard["inventory"]:
                insistence = insistence - 0.25
            if "fire" not in self.blackboard["inventory"]:
                insistence = insistence - 0.25
            Insistences.append(insistence)
        if "wood" in self.blackboard["needs"]:
            Insistences.append(self.chopping)
        return sorted(Insistences, reverse=True)[0]
