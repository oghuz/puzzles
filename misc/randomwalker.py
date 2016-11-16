#!/usr/bin/env python
from collections import defaultdict
from collections import Counter
import random

class NodeType:
    RESTAURANT = 0
    FOOD = 1

class Node:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
class Edge:
    def __init__(self, node0, node1, score):
        self.node0 = node0
        self.node1 = node1
        self.score = score
        
class RandomWalkResult:
    def __init__(self, restaurantValue, count):
        self.restaurantValue = restaurantValue
        self.count = count
        
# Feel free to modify/add on to the behavior of the graph as you want
class Graph:
    def __init__(self):
        self.nodes = []
        self.nodesToNeighbors = defaultdict(list)
        
    def addNode(self, node):
        self.nodes.append(node)
        
    def addNodes(self, nodes):
        for node in nodes:
            self.addNode(node)
        
    def addEdge(self, node0, node1, score):
        edgeFrom0 = Edge(node0, node1, score)
        edgeFrom1 = Edge(node1, node0, score)
        self.nodesToNeighbors[node0].append(edgeFrom0)
        self.nodesToNeighbors[node1].append(edgeFrom1)
        
    def getNeighbors(self, node):
        return self.nodesToNeighbors[node]
    
    def walk(self, visited, node): 
        neighbors = self.getNeighbors(node)
        candidates = [(i,n.score) for i,n in enumerate(neighbors) if n.node1 not in visited]
        nextNode = None 
        if len(candidates) >0:
            weights = [t[1] for t in candidates]
            index = self.pickBasedOnWeights(weights)
            nextNode = neighbors[candidates[index][0]].node1

        #if nextNode is not None:
        #    print "%s-%s " %(node.value, nextNode.value)
        return nextNode
    
    def pickBasedOnWeights(self, weights):
        r = random.uniform(0, sum(weights))
        step = 0
        for i, w in enumerate(weights):
            step += w
            if r <= step: 
                return i
        return -1
        
    def randomlyWalk(self, startingNode, numRandomWalks):
        # TODO: Implement
        #   Returns a sorted list of RandomWalkResults
        freq = Counter()
        dest = startingNode
        visited = set()
        visited.add(dest)
        while numRandomWalks > 0:
            dest = self.walk(visited,dest)
            if dest is None or dest.type == NodeType.RESTAURANT:
                if not dest is None:
                    freq[dest.value] +=1 
                dest = startingNode
                visited.clear()
                visited.add(dest)
                numRandomWalks -=1
            visited.add(dest)
            
        res = [RandomWalkResult(name,count) for name, count in freq.iteritems()]
        res = sorted(res, key=lambda r: r.count, reverse=True)
        #for name, count in freq.iteritems():
        #    print "%s -- %d" %(name,count)
        return res 
##### TEST CASES ######

taco = Node(NodeType.FOOD, 'taco')
burrito = Node(NodeType.FOOD, 'burrito')
spaghetti = Node(NodeType.FOOD, 'spaghetti')

tacoBell = Node(NodeType.RESTAURANT, 'taco bell')
oliveGarden = Node(NodeType.RESTAURANT, 'olive garden')

def testOneEdgeCase():
    graph = Graph()
    graph.addNode(taco)
    graph.addNode(tacoBell)
    graph.addEdge(taco, tacoBell, 1)
    randomWalks = graph.randomlyWalk(taco, 1)
    
    assert len(randomWalks) == 1
    assert randomWalks[0].count == 1
    assert randomWalks[0].restaurantValue == 'taco bell'
    
def testDisconnectedGraph():
    graph = Graph()
    graph.addNodes([taco, tacoBell])
    randomWalks = graph.randomlyWalk(taco, 1000)
    assert len(randomWalks) == 0
    
def testTwoEdgesOneEmptyCase():
    graph = Graph()
    graph.addNodes([taco, spaghetti, tacoBell])
    graph.addEdge(taco, tacoBell, 100)
    graph.addEdge(spaghetti, tacoBell, 0)
    randomWalks = graph.randomlyWalk(taco, 1)
    assert len(randomWalks) == 1
    assert randomWalks[0].count == 1
    assert randomWalks[0].restaurantValue == 'taco bell'
    
def testTree():
    print "##############################################"
    graph = Graph()
    graph.addNodes([taco, burrito, spaghetti, tacoBell, oliveGarden])
    graph.addEdge(taco, burrito, 90)
    graph.addEdge(taco, spaghetti, 10)
    graph.addEdge(burrito, tacoBell, 1)
    graph.addEdge(spaghetti, oliveGarden, 1)
    randomWalks = graph.randomlyWalk(taco, 1000)
    assert len(randomWalks) == 2;
    assert randomWalks[0].count >= 800;
    assert randomWalks[0].restaurantValue == "taco bell" 
    assert randomWalks[1].count <= 200;
    assert randomWalks[1].restaurantValue == "olive garden"
    
testOneEdgeCase()
testDisconnectedGraph()
testTwoEdgesOneEmptyCase()
testTree()

print "All tests pass!"

