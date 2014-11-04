import random
from random import randint
from node import Nodes

class Feelings:

    def __init__(self):
		#Actual feelings to be inserted
        self.outside_list = []
        external_file = '/home/ballester/Documents/lamsa/pyNeural_Emotions/config/external.in'
        try:
            self.fid = open(external_file)
        except:
            raise NameError('Wrong external input file path')


	#verify the existance of external inputs to be inserted
    def verifyExternal(self):
        try:
            aux = self.fid.readline()
        except:
            return False
			
        return aux 
		
		
	

	#minimal and maximum of the probability involved for confirmation - 0, 10	
    def compute(self, dev, up_dev, nodes):
        external = self.verifyExternal()
        #print external
        if external != False:
            external = external.split()
            aux = random.uniform(0.0, 100.0)
            #confirmado
            if aux < float(external[4]):
                #print external[0], '- aqui'
                nodes.externalInput(external[0], up_dev, random.uniform((float(external[2])-dev), float(external[2])+dev)/10.0)
            
			
            else:
                nodes.externalInput(external[1], up_dev, random.uniform((float(external[3])-dev), float(external[3])+dev)/10.0)
                #print 'disconfirmado'
			
			
	
