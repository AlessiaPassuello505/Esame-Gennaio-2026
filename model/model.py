import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph=nx.Graph()
        self._idMapC={}


    def getYears(self):
        return DAO.getAllYears()

    def creaGrafo(self,annoI,annoF):
        self._graph.clear()
        nodi = DAO.getNodi(annoI, annoF)
        for n in nodi:
            self._idMapC[n.constructorId] = n
            self._graph.add_node(n)

        archi = DAO.getArchi(annoI, annoF, self._idMapC)
        for a in archi:
            self._graph.add_edge(a.d1, a.d2, weight=float(a.peso))









    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)


