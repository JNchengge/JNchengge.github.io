from functools import partialmethod
class Cell(object):
    def __init__(self):
        self._alive=False
    @property
    def alive(self):
        return self._alive
    def set_state(self,state):
        self._alive=bool(state)
    set_alive=partialmethod(set_state,True)
    set_death=partialmethod(set_state,False)

c=Cell()
print(c.alive)
c.set_alive()
print(c.alive)