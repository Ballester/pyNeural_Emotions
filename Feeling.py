import random
from random import randint
from node import Nodes

class Feelings:

    def __init__(self):
        pass
		#Actual feelings to be inserted

	#minimal and maximum of the probability involved for confirmation - 0, 10	
    def compute(self, dev, up_dev, nodes, final_input, mag):
        confirm = random.uniform(0.0, 100.0)
        if confirm < 95.0:
            #print external[0], '- aqui'
            return nodes.externalInput(final_input[0], up_dev, random.uniform((float(mag)-dev), float(mag)+dev)/10.0)
        
        else:
            return nodes.externalInput(final_input[1], up_dev, random.uniform((float(mag)-dev), float(mag)+dev)/10.0)
            #print 'disconfirmado'
		
			
	
