from math import pi, exp
from scipy import signal
gauss = signal.gaussian(51, std=10)

def normalize(x, y):
	return x/(x+y)

'''
peso = 1.00
for h in range(0,5):
	j = 0.9
	i = 0.1
	peso += 0.02
	print "Peso: ", peso
	for k in xrange(5):
		nodo1 = i
		nodo2 = j
		aux1 = nodo1 * (1 + nodo1 + (window[25] * peso * nodo2))
		aux2 = nodo2 * (1 + nodo2 + (window[25] * peso * nodo1))
		aux3 = normalize(aux1, aux2)
		aux4 = normalize(aux2, aux1)
		print "Estimulo: ", i, "", j, " - ", aux1, " ", aux2, " -> ", aux3, aux4
		aux1 = nodo1 * (1 + nodo1 + (window[25] * -peso * nodo2))
		aux2 = nodo2 * (1 + nodo2 + (window[25] * -peso * nodo1))
		aux3 = normalize(aux1, aux2)
		aux4 = normalize(aux2, aux1)
		print "Inibicao: ", i, "", j, " - ", aux1, " ", aux2, " -> ", aux3, aux4
		i += 0.1
		j -= 0.1
'''
