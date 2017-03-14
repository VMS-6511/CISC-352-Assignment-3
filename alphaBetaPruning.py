import math
class Vertex:

    def __init__(self,value,minimaxValue, rootNodeValue):
        self.value = value
        self.neighbours = []
        self.minimaxValue = minimaxValue
        self.alpha = -float('infinity')
        self.beta = float('infinity')
        if(value.isdigit()):
            self.goalNode = True
            self.value = int(value)
        else:
            self.goalNode = False
        self.rootNode = rootNodeValue

    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value = value

    def getNeighbours(self):
        return self.neighbours
    def addVertexToNeighbours(self,vertexToAdd):
        self.neighbours.update(vertexToAdd)
    def setNeighbours(self,neighbours):
        self.neighbours = neighbours

    def getMinimaxValue(self):
        return self.minimaxValue
    def setMinimaxValue(self,minimaxValue):
        self.minimaxValue = minimaxValue

    def getAlpha(self):
        return self.alpha
    def setAlpha(self,alpha):
        self.alpha = alpha

    def getBeta(self):
        return self.beta
    def setBeta(self,beta):
        self.beta = beta

    def isGoalNode(self):
        return self.goalNode

    def isRootNode(self):
        return self.rootNode
    def __str__(self):
        string = "Value: " + str(self.value) + " Neighbours: [ " + str(self.neighbours)
        '''for x in self.neighbours:
            string = string+str(x)

        string= string + "] Minimax Value: " + self.minimaxValue'''

        return string



def alpha_beta(current_node, alpha, beta,numLeafNodes):
    #print current_node
    if current_node.isRootNode():
        current_node.alpha = -float('infinity')
        current_node.beta = float('infinity')

    if current_node.isGoalNode() == True and current_node.getMinimaxValue() == "None":
        print current_node.goalNode
        numLeafNodes = numLeafNodes+1
        print (current_node.getValue(),numLeafNodes)[0]

    elif current_node.getMinimaxValue() == "MAX":
        print current_node
        current_node.alpha = max(current_node.alpha,(alpha_beta(current_node.neighbours[0],current_node.alpha,current_node.beta,numLeafNodes)[0]))
        if current_node.alpha >= current_node.beta:
            return (current_node.alpha,numLeafNodes)

    elif current_node.getMinimaxValue() == "MIN":
        #print alpha_beta(current_node.neighbours[0],current_node.alpha,current_node.beta,numLeafNodes)
        #print current_node
        current_node.beta = min(current_node.beta,(alpha_beta(current_node.neighbours[0],current_node.alpha,current_node.beta,numLeafNodes)[0]))

        if current_node.beta <= current_node.alpha:
            return (current_node.beta,numLeafNodes)

def main():
    vertex4D = Vertex('4','None',False)
    vertex3D = Vertex('3','None',False)
    vertexD = Vertex('D','MAX',False)
    vertexD.setNeighbours([vertex4D,vertex3D])

    vertex2E = Vertex('2','None',False)
    vertex7E = Vertex('7','None',False)
    vertexE = Vertex('E','MAX',False)
    vertexE.setNeighbours([vertex2E,vertex7E])

    vertexB = Vertex('B','MIN',False)
    vertexB.setNeighbours([vertexD,vertexE])

    vertex3F = Vertex('3','None',False)
    vertex2F = Vertex('2','None',False)
    vertexF = Vertex('F','MAX',False)
    vertexF.setNeighbours([vertex3F,vertex2F])

    vertex2G = Vertex('2','None',False)
    vertex8G = Vertex('8','None',False)
    vertexG = Vertex('G','MAX',False)
    vertexG.setNeighbours([vertex2G,vertex8G])

    vertexC = Vertex('C','MIN',False)
    vertexC.setNeighbours([vertexF,vertexG])

    vertexA = Vertex('A','MAX',True)
    vertexA.setNeighbours([vertexB,vertexC])

    print(alpha_beta(vertexA,-float("infinity"),float("infinity"),0))


main()


