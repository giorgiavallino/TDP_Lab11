import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._colours = DAO.getAllColours()
        self._graph = nx.Graph()

        