from Graphs.graph import graph

g=graph()

g.addVertex('V0')
g.addVertex('V1')
g.addVertex('V2')
g.addVertex('V3')
g.addVertex('V4')

g.addEdge('V1','V2',3)
g.addEdge('V1','V4',3)
g.addEdge('V0','V1',1)
g.addEdge('V0','V3',2)
g.addEdge('V2','V4',2)
g.addEdge('V2','V0',2)
g.addEdge('V2','V3',1)

print(g)


