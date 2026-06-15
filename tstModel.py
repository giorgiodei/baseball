from model.model import Model

myModel = Model()
myModel.getTeamsOfYear(2012)
myModel.creaGrafo()
nodi, archi=myModel.getGpraphDetails()
print(f"Grafo creato con {nodi} nodi e {archi} archi")