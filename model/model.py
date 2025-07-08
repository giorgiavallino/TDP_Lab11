import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._colours = DAO.getAllColours()
        self._graph = nx.Graph()

    def buildGraph(self, colore, anno):
        self.addAllNodes(colore)
        self.addAllEdges(colore, anno)

    def addAllNodes(self, colore):
        prodotti = DAO.getAllProductsByColour(colore)
        self._graph.add_nodes_from(prodotti)

    def addAllEdges(self, colore, anno):
        nodes = self._graph.nodes
        for vertice_01 in nodes:
            for vertice_02 in nodes:
                if vertice_01 != vertice_02:
                    arco = DAO.getEdge(colore, anno, vertice_01.Product_number, vertice_02.Product_number)
                    if arco is not None and arco[0] is not None and arco[1] is not None and arco[2] is not None:
                        self._graph.add_edge(arco[0], arco[1], weight=arco[2])

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()