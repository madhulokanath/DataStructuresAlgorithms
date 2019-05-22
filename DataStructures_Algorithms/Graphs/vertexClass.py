class Vertex:

    def __init__(self,key):
        self.key=key
        self.connectedTo={}

    def add_neighbour(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def getid(self):
        return self.key

    def getConnection(self,key):
        return self.connectedTo.keys()

    def getweight(self,key):
        return self.connectedTo[key]

    def __str__(self):
        return str(self.key)+'Connected To'+str([x.key for x in self.connectedTo])



