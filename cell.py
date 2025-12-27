# base building block




class Cell:
    def __init__(self, code):
        self.code = code
        self.position = (0, 0)
        self.velocity = (0, 0)
        self.acceleration = (0, 0)

