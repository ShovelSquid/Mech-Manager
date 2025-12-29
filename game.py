# more like the gamestate but yeah

from lupa.lua54 import LuaRuntime
import lupa
lua = LuaRuntime(unpack_returned_tuples=True)

# s = lua.eval('53 * 2')
# print(s)
# zesty_func = lua.eval('function(f, n) return f(n) end')

# def func(n):
#     return n*n

# g = zesty_func(func, 3)
# print(g)
# print(lupa.lua_type(zesty_func))
# print(lupa.lua_type(s))

# def update(t):
#     print("update game by time t")


upgrades = {
    "friend": {
        "add_amount": 1
    }
}

class Upgrade:
    def __init__(self, blueprint):
        self.name = blueprint
        a = upgrades[blueprint]["add_amount"]
        self.add_amount = a if a is not None else 0



class Game:
    def __init__(self, cookies):
        self.cookies = 0 or cookies
        self.upgrades = []
        self.add_amount = 1
        self.add_amount_base = 1

    def add_cookies(self, n=None):
        self.cookies += n if n is not None else self.add_amount
        return self.cookies

    def remove_cookies(self, n=None):
        self.cookies -= n if n is not None else self.add_amount
        return self.cookies
    
    def get_scale(self):
        return 1 + self.cookies/100
    
    def add_upgrade(self, blueprint, n=None):
        if n:
            for _ in range(n):
                self.add_upgrade(blueprint)
        self.upgrades.append(Upgrade(blueprint))
        self.update_upgrade_values()
        return self.upgrades
    
    def update_upgrade_values(self):
        print("UPGRADED ADD AMOUNT: ", self.set_total_add_amount())
    
    def set_total_add_amount(self):
        amt = self.add_amount_base
        for upgrade in self.upgrades:
            amt += upgrade.add_amount
        self.add_amount = amt
        return self.add_amount
    
    def get_upgrades(self):
        ups = []
        for upgrade in self.upgrades:
            ups += upgrade
        return ups


class Cookie:
    def __init__(self, blueprint, position):
        self.name = blueprint
        self.position = position if position is not None else [0, 0]
        self.direction = [0, 0]
        self.scale = 1
        return


class Runtime:
    def __init__(self):
        self.cookies = []
        return