import time
#import Gaussian
from node import Nodes
from Feeling import Feelings
from external_input import ExternalInput
import networkx as nx
import matplotlib.pyplot as plot


#Configuration file:
config = 'config/config.ini'

try:
	fid = open(config)	
except:
	raise NameError('Wrong configuration file path')
	

#getting the configuration available in the ini
aux = fid.readline()
aux = aux.split()
external_check_delay = float(aux[1])

aux = fid.readline()
aux = aux.split()
external_up_delay = float(aux[1])

aux = fid.readline()
aux = aux.split()
external_single_file = int(aux[1])

aux = fid.readline()
aux = aux.split()
update_delay = float(aux[1])

aux = fid.readline()
aux = aux.split()
external_deviation = float(aux[1])

aux = fid.readline()
aux = aux.split()
update_deviation = float(aux[1])

aux = fid.readline()
aux = aux.split()
max_power = float(aux[1])

aux = fid.readline()
aux = aux.split()
n_nodes = int(aux[1])

aux = fid.readline()
aux = aux.split()
n_edges = int(aux[1])

aux = fid.readline()
aux = aux.split()
wt = int(aux[1])

nodes = Nodes(max_power)
external = ExternalInput(external_deviation, update_deviation)

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
    #Difference in the time of reading:
    aux_rel = nodes.edges_rel.append(-float(aux[3])/10**wt + 1)
	    
    edge = (aux[1], aux[2], aux_rel)
    nodes.G.add_edge(*edge)

print nodes.node_power
print nodes.edges_rel

nx.draw_circular(nodes.G)
plot.show()
time_check_update = time.time()
time_check_external = time_check_update
time_check_external_update = time_check_update

while True:

    aux = time.time()
    if aux - time_check_update > update_delay:
        time_check_update = aux
        nodes.update(update_deviation)
        print ["%.3f" % elem for elem in nodes.node_power]
        #print nodes.node_name
        
    if external_single_file == 0:
        if aux - time_check_external > external_check_delay:
            time_check_external = aux
            external.checkForExternalInput()
            
        if aux - time_check_external_update > external_up_delay:
            time_check_external_update = aux
            external.performExternalInputs(nodes)

    else:
        if aux - time_check_external > external_check_delay:
            time_check_external = aux
            if external.checkForExternalInput() == True:
                external.performExternalInputs(nodes)
    	
    
    








