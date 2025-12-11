# mech time baby!
# we're going back to python cause it's the best language.


class Mech:    
    def __init__(self, name, model, weightClass):
        self.name = name
        self.model = model
        self.weightClass = weightClass
        self.bodyParts = {
            "amount": 0,
            "parts": []
        }

class Part:
    def __init__(self, name, parts, weight):
        self.name = name
        self.parts = parts
        self.connections = {
            "amount": 0,
            "connectedTo": []
        }
        self.integrity = self.calculateIntegrity()
        self.weight = weight

    def calculateIntegrity(self):
        # must make sure to call this on each subpart before calling it on the parent,
        # don't want the integrity values to be wrong.
        totalIntegrity = 0
        for part in self.parts:
            totalIntegrity += part.integrity
        return totalIntegrity
    
    def attachTo(self, part):
        self.connections["connectedTo"].append(part)
        self.connections["amount"] += 1
    
    def detachFrom(self, part):
        if part in self.connections["connectedTo"]:
            self.connections["connectedTo"].remove(part)
            self.connections["amount"] -= 1


class Limb (Part):
    def __init__(self, mobility, canHold, **kwargs):
        super().__init__(**kwargs)
        self.mobility = mobility
        self.canHold = canHold



class Armor (Part):
    def __init__(self, armorRating, **kwargs):
        super().__init__(**kwargs)
        self.armorRating = armorRating

class Engine (Part):    
    def __init__(self, fuelType, fuelConsumption, powerOutput, **kwargs):
        super().__init__(**kwargs)
        self.fuelType = fuelType
        self.fuelConsumption = fuelConsumption
        self.powerOutput = powerOutput

class Storage(Part):
    def __init__(self, capacity, **kwargs):
        super().__init__(**kwargs)
        self.capacity = capacity
        self.items = []

class Weapon (Part):
    def __init__(self, damage, range, ammoType=None, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage
        self.range = range
        self.ammoType = ammoType