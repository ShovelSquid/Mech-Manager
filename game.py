# more like the gamestate but yeah
from lupa.lua54 import LuaRuntime
import lupa
lua = LuaRuntime(unpack_returned_tuples=True)

s = lua.eval('53 * 2')
print(s)
zesty_func = lua.eval('function(f, n) return f(n) end')

def func(n):
    return n*n

g = zesty_func(func, 3)
print(g)
print(lupa.lua_type(zesty_func))
print(lupa.lua_type(s))

def update(t):
    print("update game by time t")


class Game:
    def __init__(self, name, cookies):
        self.name = name
        self.cookies = 0 or cookies

    def add_cookies(self, n):
        self.cookies += n
        return n