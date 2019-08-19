# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:49:45 2019

@author: smehta
"""






















import csv
from py2neo import Graph
import time

def main():

    f = "/Users/smehta/Documents/GitHub/working-with-neo4j-through-python/data/test-data.csv" 
    graph = Graph("http://localhost:7474/db/data/")                            
    with open(f, 'r+') as in_file:

        reader = csv.reader(in_file, delimiter=',')
        next(reader, None)        
        batch = graph.cypher.begin()                           

        try:
            i = 0;
            j = 0;
            for row in reader:    
                if row:
                    character = strip(row[0])
                    first_name = strip(row[1])
                    last_name = strip(row[2])
                    actor = strip(row[3])
                    character_birth = strip(row[4])
                    character_death = strip(row[5])
                    allegiance = strip(row[6])
                    house = strip(row[7])
                    territory = strip(row[8])
                    region = strip(row[9])
                    query = """
                        merge (character:Character {Character: {a}, First_Name:{b}, Last_Name:{c}, Actor:{d}, Birth:{e}, Death:{f}})
                        merge (house:House{House:{g}, Allegiance:{h}})
                        merge (territory:Territory {Territory: {i}})
                        merge (region:Region {Region: {j}})
                        merge (character)-[:Of_House{House:{k}}]-(house)-[:Is_From]->(territory)-[:Is_In]->(region)
                    """
                    batch.append(query, {"a":character, "b": first_name, "c": last_name, "d":actor, "e":character_birth, "f":character_death, "g":house, "h": allegiance, "i":territory, "j":region, "k":house})
                    i += 1
                    j += 1
                batch.process()

                if (i == 1000): #submits a batch every 1000 lines read
                    batch.commit()
                    print j, "lines processed"
                    i = 0                
                    batch = graph.cypher.begin()
            else: batch.commit() #submits remainder of lines read                       
            print j, "lines processed"     

        except Exception as e:
            print e, row, reader.line_num

def strip(string): return''.join([c if 0 < ord(c) < 128 else ' ' for c in string]) #removes non utf-8 chars from string within cell

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time() - start
    print "Time to complete:", end