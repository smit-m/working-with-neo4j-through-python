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
g = Graph(host="localhost", password = "1234")


with open(wdir+'/data/test-data.csv') as input_file:
    readCSV = csv.reader(input_file, delimiter=',')
    counter = 1
    for row in readCSV:

        
        if counter == 1:
            continue

        print(row)

'''
        tx = g.begin()

        cols = row.split()

        #Nodes
        userid = Node('userid', id = cols[0])
        brand = Node('Brand', name = cols[1])
        category = Node('Category', name = cols[2])
        url = Node('URL', url = cols[3], sitename = cols[4])
        productid = Node('Product', id = cols[7], name = cols[6], price = cols[5])
        
        tx.create(userid)
        tx.create(brand)
        tx.create(category)
        tx.create(url)
        tx.create(productid)



        eventtype = cols[8]

        #Relationships
        user_interactswith_product = Relationship(userid, eventtype, productid)
        print(user_interactswith_product)
        product_madeby_brand = Relationship(productid, 'MADE_BY', brand)
        print(product_madeby_brand)
        product_belongsto_category = Relationship(productid, 'BELONGS_TO', category)
        print(product_belongsto_category)
        product_ison_url = Relationship(productid, 'IS_ON', url)
        print(product_ison_url)
#       
        tx.create(user_interactswith_product)
        tx.create(product_madeby_brand)
        tx.create(product_belongsto_category)
        tx.create(product_ison_url)
#       
        tx.commit()'''
        counter += 1

        








'''

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


'''