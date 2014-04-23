from graph import *

class puzzle(object):
	
	def __init__(self, order):
		self.label = order
		for index in range(9):
			if order[index] == '0':
				self.spot = index
				return None
	
	def transition(self, to):
		label = self.label
		blankLocation = self.spot
		newBlankLabel = str(label[to])
		newLabel = ''
		for i in range(9):
			if i == to:
				newLabel +='0'
			elif i == blankLocation:
				newLabel += newBlankLabel
			else:
				newLabel += str(label[i])
		return puzzle(newLabel)
	
	def __str__(self):
		return self.label
	
shiftDict = {}
shiftDict[0] = [1,3]
shiftDict[1] = [0,2,4] 
shiftDict[2] = [1,5] 
shiftDict[3] = [0,4,6] 
shiftDict[4] = [1,3,5,7] 
shiftDict[5] = [2,4,8] 
shiftDict[6] = [3,7] 
shiftDict[7] = [4,6,8] 
shiftDict[8] = [5,7]

def BFSWithGenerator(start, end, q =[]):
	initPath = [start]
	q.append(initPath)
	while len(q) != 0:
		tmpPath = q.pop(0)
		lastNode = tmpPath[len(tmpPath) -1]
		if lastNode.label == end.label:
			return tmpPath
		for shift in shiftDict[lastNode.spot]:
			new = lastNode.transition(shift)
			if notInPath(new, tmpPath):
				newPath = tmpPath + [new]
				q.append(newPath)
	return None

def notInPath(node, path):
	for elt in path:
		if node.label == elt.label:
			return False
	return True

def DFSWithGenerator(start, end, stack =[]):
	initPath = [start]
	stack.insert(0, initPath)
	while len(stack) != 0:
		tmpPath = stack.pop(0)
		lastNode = tmpPath[len(tmpPath) -1]
		if lastNode.label == end.label:
			return tmpPath
		for shift in shiftDict[lastNode.spot]:
			new = lastNode.transition(shift)
			if notInPath(new, tmpPath):
				newPath = tmpPath + [new]
				stack.insert(0, newPath)
	return None

#goal = puzzle('012345678')
#test1 = puzzle('125638047')

def printGrid(pzl):
	data = pzl.label
	print data[0], data[1], data[2]
	print data[3], data[4], data[5]
	print data[6], data[7], data[8]
	print '\n'

def printSolution(path):
	for elt in path:
		printGrid(elt)

def powerSet(elts):
	if len(elts) == 0:
		return [[]]
	else:
		smaller = powerSet(elts[1:])
		elt = [elts[0]]
		withElt =[]
		for s in smaller:
			withElt.append(s + elt)
		allofthem = smaller + withElt
		return allofthem
	
def powerGrpah(gr):
	nodes = gr.nodes
	nodesList =[]
	for elt in nodes:
		nodesList.append(elt)
	pSet = powerSet(nodesList)
	return pSet
	
def allConnected(gr, candidate):
	for n in candidate:
		for m in candidate:
			if not n == m:
				if n not in gr.childrenOf(m):
					return False
	return True

def maxClique(gr):
	candidates = powerGraph(gr)
	keepEm = []
	for candidate in candidates:
		if allConnected(gr, candidate):
			keepEm.append(candidate)
	bestLength = 0
	bestSoln = None
	for test in keepEm:
		if len(test) > bestLength:
			bestLength = len(test)
			bestSoln = test
	return bestSoln
	
