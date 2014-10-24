import time
#import Gaussian
from node import Nodes

#Configuration file:
config = '/home/ballester/NetBeansProjects/pyNeural_Emotions/config/config.ini'

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

nodes = Nodes()

for i in xrange(n_nodes):
	aux = fid.readline()
	aux = aux.split()
	nodes.nodes.append(aux[0])
	nodes.edges_from.append(int(aux[1]))
	nodes.edges_to.append(int(aux[2]))
	print nodes.nodes

