import math
class Vertex:

    def __init__(self,value,minimaxValue):
        self.value = value
        self.neighbours = {}
        self.minimaxValue = minimaxValue
        self.alpha = -math.inf
        self.beta = math.inf

