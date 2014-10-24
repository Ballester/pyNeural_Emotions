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
	nodes.node_name.append(aux[0])
	nodes.node_number.append(int(aux[2]))
	nodes.node_level.append(int(aux[2]))
	
for i in xrange(n_edges):
	aux = fid.readline()
	aux = aux.split()
	nodes.edges_from.append(int(aux[1]))
	nodes.edges_to.append(int(aux[2]))
	print nodes.edges_from
