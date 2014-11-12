from math import pi, exp
from scipy import signal
from random import randint
import networkx as nx

#todo: Add thread for external input and update
class Nodes:
    
    #Max_power still \todo
    def __init__(self, max_power):
        self.max_power = max_power
        self.G = nx.Graph()
        self.node_name = []
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
        for i in xrange(len(self.node_name)):
            aux.append(-1)
            qt.append(0)

        #Calculate the new values:
        for i in xrange(len(self.edges_from)):
            pos_from = self.node_name.index(self.edges_from[i])
            pos_to = self.node_name.index(self.edges_to[i])
            #if self.edges_rel[i] > 0.0:
            aux[pos_to] = self.node_power[pos_to] * (1 + self.node_power[pos_to] + (self.window[randint(20,30)] * self.edges_rel[i] * self.node_power[pos_from]))
           
            
            #print aux[pos_to], " - ", self.node_name[pos_to]
            qt[pos_to] += 1

        #Case if there is more than one relation:
        for i in xrange(len(self.node_level)):
            if aux[i] != -1:
                self.node_power[i] = float(aux[i]/qt[i])
            if aux[i] < 0.0:
                self.node_power[i] = 0.0                

                
        #Normalize by level:
        for i in xrange(max(self.node_level)+1):
            count = 0.0
            for j in xrange(len(self.node_level)):
                if self.node_level[j] == i:
                    count += self.node_power[j]
            
            for j in xrange(len(self.node_level)):
                if self.node_level[j] == i: 
                    #print count, " ", i
                    self.node_power[j] /= count
                    
                    
    def externalInput(self, feeling, up_dev, power):
        print feeling
        for i in xrange(len(self.node_name)):
            if self.node_name[i] == feeling:
                self.node_power[i] += power
                print 'Input in node - ', self.node_name[i], ' - ', power
                self.update(up_dev)
                return True

        return False
            
            
            
                



                
                

