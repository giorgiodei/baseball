import copy
import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._teams=[]
        self._idMapTeams = None
        self._bestPath=[]
        self._bestObjVal=0





    def getPath(self,v0):
        self._bestPath = []
        self._bestObjVal = 0
        parziale=[v0]
        for v in self._grafo.neighbors(v0):
            parziale.append(v)
            self._ricorsione(parziale)
            parziale.pop()

    def _ricorsione(self, parziale):
        if self._score(parziale) > self._bestObjVal:
            self._bestPath = copy.deepcopy(parziale)
            self._bestObjVal = self._score(parziale)

        for v in self._grafo.neighbors(parziale[-1]):
            pesoE=self._grafo[parziale[-1]][v]["weight"]

            if self._grafo[parziale[-2]][parziale[-2]]["weight"] > pesoE and v not in parziale:

                parziale.append(v)
                self._ricorsione(parziale)
                parziale.pop()


    def _score(self,parziale):
        score=0
        for i in range(0,len(parziale)-1):
            score+=self._grafo[parziale[i]][parziale[i+1]]["weight"]

    def _ricorsione(self):
        pass


    def getAllYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self._teams = DAO.getTeamsOfYear(year)
        self._idMapTeams = {t.ID: t for t in self._teams}
        return self._teams

    def creaGrafo(self, year):
        self._grafo.clear()

        self._grafo.add_nodes_from(self._teams)
        """for u in self._grafo.nodes():
            for v in self._grafo.nodes():
                if v!=u:
                    self._grafo.add_edge(u, v)"""

        myedges=itertools.combinations(self._teams, 2)
        self._grafo.add_edges_from(myedges)



        mapSalary=DAO.getSalariesTeam(year,self._idMapTeams)
        for e in self._grafo.edges:
            sal1 = mapSalary.get(e[0], 0)
            sal2 = mapSalary.get(e[1], 0)
            peso = sal1 + sal2
            self._grafo[e[0]][e[1]]["weight"] = peso


        print("test")


    def getVicini(self, source):
        vicini=self._grafo.neighbors(source)
        viciniTuples=[]
        for v in vicini:
            viciniTuples.append((v,self._grafo[source][v]["weight"]))

        viciniTuples.sort(key=lambda x: x[1], reverse = True)

        return viciniTuples



    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)