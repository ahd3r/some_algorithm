# from time import sleep
import random

# def print_item_of_mas(mas):
# 	for item in mas:
# 		sleep(1)
# 		print(item)

# print_item_of_mas([1,2,3,4,5,6,7,8,9])

# def qs(mas):
# 	if len(mas)<=1:
# 		return mas
# 	else:
# 		pivot=mas[0]
# 		less_then_pivot=[i for i in mas[1:] if i <= pivot]
# 		more_then_pivot=[i for i in mas[1:] if i > pivot]
# 		return qs(less_then_pivot)+[pivot]+qs(more_then_pivot)

# print(qs([36,256,32,76,36,4326,543,4,85,3,1,534,7,653,473]))
#---------------------------------------------------------------------
# 1
# The task of finding the easiest way for graph with some weight
class Graph():
	def __init__(self, lengh, weight): # lengh — lengh of graph without start and end; weight — mas of weight, which will take by randint for weight of ribs
		self.lengh=lengh
		self.weight=weight
		self.res_way=[]
		self.res_weight=None
		self.node=[]
		self.connect={}

	def __str__(self):
		return 'Class for count the easiest way for graph with some weight!'

	def create_a_node_for_graph(self):
		self.node.append('(1,start)')
		for x in range(self.lengh):
			for y in range(random.randint(1,3)): # level
				self.node.append(f'({x + 2}.{y+1})')
		self.node.append(f'({self.lengh + 2},finish)')
		return self.node

	def create_a_connections_for_graph(self):
		for c in range(len(self.node)):
			self.connect[f'{self.node[c]}:>{self.node[c]}'] = random.choice(self.weight)
		return self.connect

	def find_the_way(self):
		return self.res_way, self.res_weight

g=Graph(lengh=3,weight=[1,2,3,4])
print(g.create_a_node_for_graph())
print(g.create_a_connections_for_graph())
print(g.find_the_way())

# The task of finding the easiest way for graph with some weight include negative

# The task of finding the shortest way for graph without some weight

# The graph without directions

# 2
# The task of covering states

# 3
# The task of traveling Camewoyzer