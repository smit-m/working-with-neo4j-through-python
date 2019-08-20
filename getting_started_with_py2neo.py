# -*- coding: utf-8 -*-

#########################################################################
### Authors: Smit Mehta
### Python:  Version 3.7
### Details: Getting started with py2neo using the resource: Py2neo v3 Handbook (https://py2neo.org/v3/index.html)
#########################################################################


from py2neo import Graph, Node, Relationship
import csv


g = Graph(host="localhost", password = "1234")
tx = g.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)
tx.create(ab)
tx.commit()
g.exists(ab)