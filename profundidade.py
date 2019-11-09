 # -*- coding: utf-8 -*-
class Vertice(object):
	def __init__(self):
		self.antecessorVertice = {}
		self.profundidade = {}

	def iniciaVertices(self, v):
		self.antecessorVertice[v] = v
		self.profundidade[v] = 0

	def encontraVerticeAntecessor(self, v):
		if self.antecessorVertice[v] == v:
			return self.antecessorVertice[v]
		else:
			return self.encontraVerticeAntecessor(self.antecessorVertice[v])

	def equilibraVerticeAntecessor(self, v1, v2):
		if self.profundidade[v1] > self.profundidade[v2]:
			self.antecessorVertice[v2]= self.antecessorVertice[v1]
			self.profundidade[v2] = self.profundidade[v1] + 1
		elif self.profundidade[v1] == self.profundidade[v2]:
			self.antecessorVertice[v2] = self.antecessorVertice[v1]
			self.profundidade[v2]= self.profundidade[v2] + 1

class Aresta(object):
	def __init__(self, v1, v2, peso):
		self.v1 = v1
		self.v2 = v2
		self.peso = peso

class Grafo(object):
	def __init__(self):
		self.vertices = []
		self.arestas = []
		self.arvoreGeradora = []
		self.distancias = {}
	
	def adicionaArestas(self, Aresta):
		self.arestas.append(Aresta)

	def eParente(self):
		v = Vertice()

		for i in self.vertices:
			v.iniciaVertices(i)

		self.arestas.sort(key=lambda x: x.peso)
		
		for i in self.arestas:
			v1 = v.encontraVerticeAntecessor(i.v1)
			v2 = v.encontraVerticeAntecessor(i.v2)
			if v1 != v2:
				print(i.v1, i.v2)
				self.arvoreGeradora.append(i)
				v.equilibraVerticeAntecessor(v1, v2)

	def imprimeGrafo(self):
		x = 1
		for i in self.arestas:
			print '{}º Aresta: {}-{}\nPeso: {}'.format(x, i.v1, i.v2, i.peso)
			print
			x = x + 1
		return x - 1

	def imprimeArvoreGeradora(self):
    		x = 1
		pesoTotal = 0
		for i in self.arvoreGeradora:
			print '{}º Aresta: {}-{}\nPeso: {}'.format(x ,i.v1, i.v2, i.peso)
			print
			pesoTotal = pesoTotal + i.peso	
			x = x + 1
		return x - 1, pesoTotal

def main():

	grafo = Grafo()
	grafo.vertices = ['1','2','3','4','5','6','7','8','9','10']
	
	aresta12 = Aresta('1','2', 25)
	grafo.adicionaArestas(aresta12)
	aresta13 = Aresta('1','3', 17)
	grafo.adicionaArestas(aresta13)
	aresta17 = Aresta('1','7', 24)
	grafo.adicionaArestas(aresta17)
	aresta18 = Aresta('1','8', 22)
	grafo.adicionaArestas(aresta18)
	aresta19 = Aresta('1','9', 4)
	grafo.adicionaArestas(aresta19)
	aresta110 = Aresta('1','10', 11)
	grafo.adicionaArestas(aresta110)

	aresta23 = Aresta('2','3', 20)
	grafo.adicionaArestas(aresta23)
	aresta24 = Aresta('2','4', 11)
	grafo.adicionaArestas(aresta24)
	aresta25 = Aresta('2','5', 15)
	grafo.adicionaArestas(aresta25)

	aresta34 = Aresta('3','4', 13)
	grafo.adicionaArestas(aresta34)
	aresta37 = Aresta('3','7', 24)
	grafo.adicionaArestas(aresta37)
	aresta39 = Aresta('3','9', 1)
	grafo.adicionaArestas(aresta39)
	aresta310 = Aresta('3','10', 16)
	grafo.adicionaArestas(aresta310)

	aresta47 = Aresta('4','7', 6)
	grafo.adicionaArestas(aresta47)
	aresta48 = Aresta('4','8', 7)
	grafo.adicionaArestas(aresta48)
	aresta49 = Aresta('4','9', 24)
	grafo.adicionaArestas(aresta49)

	aresta56 = Aresta('5','6', 21)
	grafo.adicionaArestas(aresta56)
	aresta57 = Aresta('5','7', 21)
	grafo.adicionaArestas(aresta57)
	aresta510 = Aresta('5','10', 3)
	grafo.adicionaArestas(aresta510)

	aresta67 = Aresta('6','7', 15)
	grafo.adicionaArestas(aresta67)
	aresta610 = Aresta('6','10', 18)
	grafo.adicionaArestas(aresta610)

	aresta78 = Aresta('7','8', 23)
	grafo.adicionaArestas(aresta78)
	
	print '/------------------------------------GRAFO ORIGINAL'
	x = grafo.imprimeGrafo()
	print x, 'Arestas do Grafo Original'
	grafo.eParente()
	print '/----------------------------------Parente RESULTADO'
	#x, peso = grafo.imprimeArvoreGeradora()
	#print x, 'Arestas na Árvore Geradora\nC(MST) = {}\n'.format( peso)

main()	