from math import pi, exp
from scipy import signal

class Nodes:
    
    def __init__(self):
        self.node_name = []
        self.node_number = []
        self.node_level = []
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

        for i in xrange(len(self.edges_from)):
            pos_from = self.edges_from[i]
            pos_to = self.edges_to[i]
            aux[pos_to] = self.node_level[pos_to] * (1 + self.node_level[pos_to] + (self.window[25] * self.edges_rel[i] * self.node_level[pos_from]))
            
            qt[pos_to] += 1

        for i in xrange(len(self.node_level)):
            print i
            if aux[i] != -1:
                self.node_level[i] = float(aux[i]/qt[i])

