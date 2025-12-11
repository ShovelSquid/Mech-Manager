# store where you can buy items, sell items, get them delivered


class Economy:
    def __init__(self):
        self.markets = {
            "amount": 0,
            "markets": []
        }


class Market:
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory
    
    def addItem(self, item):
        self.inventory["items"].append(item)
        self.inventory["amount"] += 1

    def removeItem(self, item):
        if item in self.inventory["items"]:
            self.inventory["items"].remove(item)
            self.inventory["amount"] -= 1

    def listItems(self):
        return self.inventory["items"]
    
    def findItem(self, itemName):
        for item in self.inventory["items"]:
            if item.name == itemName:
                return item
        return None
    
    def updateItemPrice(self, itemName, newPrice):
        item = self.findItem(itemName)
        if item:
            item.price = newPrice
            return True
        return False
    
class Item:
    def __init__(self, name, price, quality, quantity):
        self.name = name
        self.price = price
        self.quality = quality
        self.quantity = quantity