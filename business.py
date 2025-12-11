# what mechs you have, what parts are in storage,
# what weapons do you own, who do you employ, etc.




class Business:    
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.mechs = {
            "amount": 0,
            "mechs": []
        }
        self.inventory = {
            "amount": 0,
            "items": []
        }
        self.employees = {
            "amount": 0,
            "employees": []
        }
    
    def hireEmployee(self, employee):
        self.employees["employees"].append(employee)
        self.employees["amount"] += 1
    
    def fireEmployee(self, employee):
        if employee in self.employees["employees"]:
            self.employees["employees"].remove(employee)
            self.employees["amount"] -= 1
    
    def addMech(self, mech):
        self.mechs["mechs"].append(mech)
        self.mechs["amount"] += 1
    
    def removeMech(self, mech):
        if mech in self.mechs["mechs"]:
            self.mechs["mechs"].remove(mech)
            self.mechs["amount"] -= 1
    
    def addItemToInventory(self, item):
        self.inventory["items"].append(item)
        self.inventory["amount"] += 1

    def removeItemFromInventory(self, item):
        if item in self.inventory["items"]:
            self.inventory["items"].remove(item)
            self.inventory["amount"] -= 1
    
    def buyItem(self, item, price):
        if self.money >= price:
            self.money -= price
            self.addItemToInventory(item)
            return True
        return False
    
    def sellItem(self, item, price):
        if item in self.inventory["items"]:
            self.money += price
            self.removeItemFromInventory(item)
            return True
        return False