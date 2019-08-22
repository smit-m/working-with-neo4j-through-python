# -*- coding: utf-8 -*-

#########################################################################
### Authors: Smit Mehta
### Python:  Version 3.7
### Details: Getting started with py2neo using the resource: Py2neo v3 Handbook (https://py2neo.org/v3/index.html)
#########################################################################


from py2neo import Graph, Node, Relationship
import csv
import os

wdir = os.getcwd()

with open(widr+'/data/test-data.csv') as input_file:
	readCSV = csv.reader(input_file, delimiter=',')
    for row in readCSV:
    	#do something




from py2neo import Graph, Node, Relationship

g = Graph(host="localhost", password = "1234")


firstperson = ['A', 'Harry', 'Tom']
secondperson = ['B', 'Potter', 'Jerry']


for i, j in zip(firstperson, secondperson):
	tx = g.begin()
	a = Node('Person', name = i)
	print(a)
	b = Node('Person', name = j)
	print(b)
	tx.create(a)
	print('Done 1')
	tx.create(b)
	print('Done 1.5')
	ab = Relationship(a, 'KNOWS', b)
	print(ab)
	tx.create(ab)
	print('Done 2')
	tx.commit()
	print('Done 3')




g = Graph(host="localhost", password = "1234")
tx = g.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)
tx.create(ab)
tx.commit()
g.exists(ab)