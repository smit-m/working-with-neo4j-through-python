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
tx = g.begin()

firstperson = ['John', 'Harry', 'Tom']
secondperson = ['Wick', 'Potter', 'Jerry']


for i, j in zip(firstperson, secondperson):
	a = Node('Person', name = i)
	b = Node('Person', name = j)
	tx.create(a)
	tx.create(b)
	ab = Relationship(a, 'KNOWS', b)
	tx.create(ab)
	tx.commit()




g = Graph(host="localhost", password = "1234")
tx = g.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)
tx.create(ab)
tx.commit()
g.exists(ab)