"""
CISC 352 - Assignment #3
Program #3 - Alpha-Beta Pruning
"""
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
        
    def sort(self):
        if(len(self.neighbours)>0):
            if (type(self.neighbours[0].value) is str):
                if not(self.neighbours[0].value.isdigit()):
                    self.neighbours = sorted(self.neighbours)
                
    
    def __lt__(self, other):
        if isinstance(other, Vertex):
            return self.value < other.value
        return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, Vertex):
            return self.value > other.value
        return NotImplemented

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
        string = "Value: " + str(self.value) + " Neighbours: " + str(self.neighbours)
        '''for x in self.neighbours:
            string = string+str(x)

        string= string + "] Minimax Value: " + self.minimaxValue'''

        return string

    
def alpha_beta(current_node, alpha, beta,numGoalNodes):

    if current_node.isRootNode():
        alpha = -float("infinity")
        beta = float("infinity")

    if current_node.isGoalNode():
        numGoalNodes = numGoalNodes+1
        return (current_node.getValue(),numGoalNodes)


    elif current_node.getMinimaxValue() == "MAX":
        values = []
        for child in current_node.neighbours:
            value,numGoalNodes = alpha_beta(child,alpha,beta,numGoalNodes)
            values.append(value)
            alpha = max(alpha,max(values))
            current_node.alpha = max(alpha,max(values))
            if(alpha >= beta):
                return (beta,numGoalNodes)
        return (alpha,numGoalNodes)

    elif current_node.getMinimaxValue() == "MIN":
        values = []
        for child in current_node.neighbours:
            value,numGoalNodes = alpha_beta(child,alpha,beta,numGoalNodes)
            values.append(value)
            beta = min(beta,min(values))
            current_node.beta = min(beta,min(values))
            if(beta<=alpha):
                return (alpha,numGoalNodes)
        return (beta,numGoalNodes)

"""
Given one line of input from 'alphabeta.txt'
buildGraph() creates the graph using the vertex class
return the node at the root of the graph
"""
def buildGraph(vSet):
    #Splits input into sets of nodes and edges
    vSet = vSet.split()
    nodeSet = splitEdges(vSet[0])
    edgeSet = splitEdges(vSet[1])

    #Dictionary holds vertex's in form {'value' : VertexObject} 
    vertexSet = {}
    
    #Create vertex for root node
    vertexSet[nodeSet[0][0]] = Vertex(nodeSet[0][0], nodeSet[0][1], True)
    rootVertex = vertexSet[nodeSet[0][0]]

    #Create vertex's for all other non-leaf nodes
    for node in nodeSet[1:]:
        vertexSet[node[0]] = Vertex(node[0], node[1], False)

    #Populate the neighbours array of each vertex
    #Create vertex's for leaf nodes
    for edge in edgeSet:
        node1 = edge[0]
        node2 = edge[1]
        
        if vertexSet.has_key(node2):
            vertexSet[node1].neighbours.append(vertexSet[node2])
        else:
            vertexSet[node2] = Vertex(node2, 'None', False)
            vertexSet[node1].neighbours.append(vertexSet[node2])
    
    for keyVal, value in vertexSet.iteritems():
        value.sort()
    
    return rootVertex

"""
Helper function for buildGraph()
Converts node and edge sets from string form to array form
"""
def splitEdges(edgeSet):
    edges = []
    trimInput = edgeSet[1:]
    start = 0
    end = 0
    
    for i in range(0, len(trimInput)):
        if trimInput[i] == "(":
            first = "" #will hold first atom in clause
            firstIndex = i + 1
            while trimInput[firstIndex] != ",":
                first += trimInput[firstIndex]
                firstIndex += 1
            secondIndex = firstIndex + 1
            second = "" #holds second atom in clause
            while trimInput[secondIndex] != ")":
                second += trimInput[secondIndex]
                secondIndex += 1
            i = secondIndex #increment loop counter to start of next clause
            edges.append((first, second))
            
    return edges


#Appends the results of alphaBeta Pruning to output file
def writeFile(fileName, stringOut):
    fo = open(fileName, 'a')
    fo.write(stringOut)
    fo.write("\n")

#Reads graphs from input file into array
def readFile(fileName):
    f = open(fileName, 'r')
    content = f.readlines()
    content = [x.strip() for x in content]
    return content

"""
Performs alphaBeta Pruning on graphs from input file
Writes results to output file
"""
def runProb3(fileIn, fileOut):
    contentIn = readFile(fileIn)

    graphNum = 1
    for line in range(0, len(contentIn), 2):
        graph = contentIn[line]
        rootNode = buildGraph(graph)
        solu = (alpha_beta(rootNode,0,0,0))
        stringOut = ("Graph " + str(graphNum) + ": Score: " + str(solu[0]) +
               "; Leaf Nodes Examined: " + str(solu[1]) + "\n")
        graphNum += 1
        writeFile(fileOut, stringOut)
        
def main():
    runProb3('alphabeta.txt', 'alphabeta_out.txt')

main()
