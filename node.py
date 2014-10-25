from math import pi, exp
from scipy import signal

class Nodes:
    
    def __init__(self):
        self.node_name = []
        self.node_number = []
        self.node_level = []
        self.node_power = []
        self.edges_from = []
        self.edges_to = []
        self.edges_rel = []

    def inputSignal(self, x, dev):
        self.window = signal.gaussian(x, dev)

    def update(self, stddev):
        aux = []
        qt = []
        self.inputSignal(51,10)
        for i in xrange(len(self.node_number)):
            aux.append(-1)
            qt.append(0)

        #Calculate the new values:
        for i in xrange(len(self.edges_from)):
            pos_from = self.edges_from[i]
            pos_to = self.edges_to[i]
            aux[pos_to] = self.node_power[pos_to] * (1 + self.node_power[pos_to] + (self.window[25] * self.edges_rel[i] * self.node_power[pos_from]))
            
            qt[pos_to] += 1

        #Case if there is more than one relation:
        for i in xrange(len(self.node_level)):
            if aux[i] != -1:
                self.node_power[i] = float(aux[i]/qt[i])
                
        #Normalize by level:
        for i in xrange(max(self.node_level)+1):
            count = 0.0
            for j in xrange(len(self.node_level)):
                if self.node_level[j] == i:
                    count += self.node_power[j]
            
            for j in xrange(len(self.node_level)):
                if self.node_level[j] == i: 
                    print count, " ", i
                    self.node_power[j] /= count
            
            
            
                



                
                

