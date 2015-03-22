#!/usr/bin/env python3

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

        self.skills = {"cooking":self.cooking, "hunting":self.hunting, "chopping":self.chopping, "locate":self.locate}

        self.inventory = blackboard["inventory"]
        self.tasks = []

    def executeTasks(self):
        for task in self.tasks:
            if (task == "cook"):
                if "ingredients" in inventory:
                    if(cook(food)):
                        blackboard["inventory"].append("food")
                    blackboard["inventory"].remove("ingredients")
                elif ("ingredients" not in blackboard["needs"]:
                        blackboard["needs"].append("ingredients") = []
        

    def cook(self, food_difficulty=1.0):
        if "food" in inventory:
            print("We already have food!")
            return
        if "meat" in inventory and "water" in inventory and "fire" in inventory:
            difficulty = self.cooking / food_difficulty
            result = random.random() < diffuculty
            if (result):
                print("I have successuflly cooked food. Enjoy!".format(food.string))
                    blackboard["inventory"].append("food")
            else:
                print("I screwed this dish up.  We could eat it at the risk of...Dysentery")
            blackboard["inventory"].remove("meat")
            blackboard["inventory"].remove("water")
            blackboard["inventory"].remove("fire")
        else:
            if "meat" not in inventory:
                blackboard["needs"].append("meat")
                print("We need Meat!")
            if "water" not in inventory:
                blackboard["needs"].append("water")
                print("We need Water!")
            if "fire" not in inventory:
                blackboard["needs"].append("fire")
                print("We need Fire!")

    def hunt(self, animal_difficulty=1.0):
        difficulty = self.hunting / animal_difficulty
        result = random.random() < difficulty
        if (result):
            print("I have successfully hunted {}.  Let's cook it!".format(animal.string))
            inventory.append("meat")
        else:
            print("I have failed this hunting mission.  Shall we eat our boots?")

    def chop(self wood_difficulty):
        difficulty = self.chopping  / wood_difficulty
        result = random.random() < difficulty
        if (result):
            print("I have chopped the {}.  Lets make something with this fine wood".format(wood.string))
        else:
            print("I have failed miserably and my axe has broken!")
        return result

    def survival(self resource_difficulty):
        difficulty = self.locate  / resource_difficulty
        result = random.random() < difficulty
        if (result):
            print("I have found some {}. Let's enjoy it while it lasts..".format(item.string))

    def evaluateBlackboard(self, blackboard):
        for task in blackboard["tasks"]:
            if (task in ["cooking", "hunting", "chopping", "locate"]):
                blackboard["tasks"][task].append((self, interest(task)))
        for item in blackboard["inventory"]:
            self.inventory.append(item)

    def interest(task):
        return self.skills[task]
