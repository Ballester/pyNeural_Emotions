import random
from random import randint
from node import Nodes

class Feelings:

    def __init__(self):
        config = 'config/feeling.ini'
        try:
            fid = open(config)
	        	
        except:
	        raise NameError('Wrong configuration file path')
	
        aux = fid.readline()
        aux = aux.split()
        self.bipolar_effect = float(aux[1])


	#minimal and maximum of the probability involved for confirmation - 0, 10	
    def compute(self, dev, up_dev, nodes, final_input, mag):
        confirm = random.uniform(0.0, 100.0)
        if confirm > self.bipolar_effect:
            print final_input
            return nodes.externalInput(final_input[0], up_dev, random.uniform((float(mag)-dev), float(mag)+dev)/10.0)
        
        else:
            return nodes.externalInput(final_input[1], up_dev, random.uniform((float(mag)-dev), float(mag)+dev)/10.0)
            #print 'disconfirmado'
		
			
	
