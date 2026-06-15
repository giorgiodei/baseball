import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._teams=[]
        self._idMapTeams = None


    def getAllYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self._teams = DAO.getTeamsOfYear(year)
        self._idMapTeams = {t.ID: t for t in self._grafo.nodes}
        return self._teams

    def creaGrafo(self, year):
        self._grafo.add_nodes_from(self._teams)
        """for u in self._grafo.nodes():
            for v in self._grafo.nodes():
                if v!=u:
                    self._grafo.add_edge(u, v)"""

        myedges=itertools.combinations(self._teams, 2)
        self._grafo.add_edges_from(myedges)



        mapSalary=DAO.getSalariesTeam(year,self._idMapTeams)
        for e in self._grafo.edges:
            sal1=mapSalary[e[0]]
            sal2 = mapSalary[e[1]]
            peso=sal1+sal2
            self._grafo[e[0]][e[1]]["weight"]=peso


        print("test")


    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)