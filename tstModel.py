from model.model import Model

myModel = Model()
myModel.getTeamsOfYear(2012)
myModel.creaGrafo(2012)
nodi, archi=myModel.getGraphDetails()
print(f"Grafo creato con {nodi} nodi e {archi} archi")