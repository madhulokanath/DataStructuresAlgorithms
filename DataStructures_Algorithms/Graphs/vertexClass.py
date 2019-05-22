class Vertex:

    def __init__(self,key):
        self.distance=0
        self.pred=None
        self.color='white'
        self.key=key
        self.connectedTo={}

    def add_neighbour(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def getid(self):
        return self.key

    def getConnections(self):
        return self.connectedTo.keys()

    def getweight(self,key):
        return self.connectedTo[key]

    def __str__(self):
        return str(self.key)+'Connected To'+str([x.key for x in self.connectedTo])

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color=color

    def setDistance(self,dist):
        self.distance=dist

    def getDistance(self):
        return self.distance

    def setPred(self,pred):
        self.pred=pred

    def getPred(self):
        return self.pred





