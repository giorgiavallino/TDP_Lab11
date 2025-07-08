from model.model import Model

m = Model()
m.buildGraph("White", 2018)
print(m.getNumNodes())
print(m.getNumEdges())