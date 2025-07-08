import itertools
from collections import Counter

import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._colours = DAO.getAllColours()
        self._prodotti = None
        self._idMapProdotti = {}
        self._graph = nx.Graph()

    def buildGraph(self, colore, anno):
        self._graph.clear()
        self.addAllNodes(colore)
        self.addAllEdges(colore, anno)

    def addAllNodes(self, colore):
        self._prodotti = DAO.getAllProductsByColour(colore)
        self.createIdMapProdotti()
        self._graph.add_nodes_from(self._prodotti)

    def createIdMapProdotti(self):
        for prodotto in self._prodotti:
            self._idMapProdotti[prodotto.Product_number] = prodotto

    def addAllEdges(self, colore, anno):
        for node_01, node_02 in itertools.combinations(self._graph.nodes, 2):
            prodotto_01 = int(node_01.Product_number)
            prodotto_02 = int(node_02.Product_number)
            arco = DAO.getEdge(colore, anno, prodotto_01, prodotto_02)
            if arco is not None and arco[0] is not None and arco[1] is not None:
                self._graph.add_edge(self._idMapProdotti[arco[0]], self._idMapProdotti[arco[1]], weight=arco[2])

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getArchiPesoMaggiore(self):
        archi = list(self._graph.edges(data=True))
        archi.sort(key=lambda a:a[2]["weight"], reverse=True)
        return archi[:3]

    def getProdottiPiùPresenti(self):
        archiPesoMaggiore = self.getArchiPesoMaggiore()
        nodi = []
        for arco in archiPesoMaggiore:
            nodi.append(arco[0])
            nodi.append(arco[1])
        counter = Counter(nodi)
        result = []
        for element in counter:
            if counter[element] > 1:
                result.append(element)
        return result