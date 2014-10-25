import time
#import Gaussian
from node import Nodes
import networkx as nx
import matplotlib.pyplot as plot

#Configuration file:
config = '/home/ballester/Documents/pyNeural_Emotions/config/config.ini'

try:
	fid = open(config)	
except:
	raise NameError('Wrong configuration file path')
	

#getting the configuration available in the ini
aux = fid.readline()
aux = aux.split()
n_nodes = int(aux[1])

aux = fid.readline()
aux = aux.split()
n_edges = int(aux[1])

aux = fid.readline()
aux = aux.split()
wt = int(aux[1])

nodes = Nodes()

for i in xrange(n_nodes):
	aux = fid.readline()
	aux = aux.split()
	nodes.node_name.append(aux[0])
	nodes.G.add_node(aux[0])
	nodes.node_level.append(int(aux[1]))
	nodes.node_power.append(float(aux[2]))
	
for i in xrange(n_edges):
	aux = fid.readline()
	aux = aux.split()
	nodes.edges_from.append(aux[1])
	nodes.edges_to.append(aux[2])
	nodes.edges_rel.append(float(aux[3])/10**wt + 1)
	edge = (aux[1],aux[2])
	nodes.G.add_edge(*edge)

nx.draw(nodes.G)
plot.show()
while True:
    print nodes.node_power
    nodes.update(10)
    time.sleep(2)







