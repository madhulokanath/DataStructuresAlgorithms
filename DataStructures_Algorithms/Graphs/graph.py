from Graphs.vertexClass import Vertex
from BasicDS.Q import Queue
class graph:
    def __init__(self):
        self.vertList={}
        self.numberofVertices=0

    def addVertex(self,key):
        self.numberofVertices=self.numberofVertices+1
        newvertex=Vertex(key)
        self.vertList[key]=newvertex
        return newvertex

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return 'No such vertex present in the graph'

    def deleteVertex(self,key):
        if key in self.vertList:
            self.vertList.pop(key)
            self.numberofVertices=self.numberofVertices-1
            return key
        else:
            return 'No such vertext present in the graph'

    def getVertices(self):
        return self.vertList.keys()

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].add_neighbour(self.vertList[t],cost)

    def __contains__(self,n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def __str__(self):
        print('Graph contains :'+str(self.numberofVertices)+' vertices ==> '+str([x for x in self.vertList]) )
        for a in self.vertList:
            print(self.vertList[a])
        return 'End'

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getid())
        x = x.getPred()
    print(x.getid())






