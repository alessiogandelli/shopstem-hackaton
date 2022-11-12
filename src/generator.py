#%%

import time
import numpy as np
import pandas as pd
import datetime
import csv
import time
from random import seed
from random import randint
import numpy as np
import matplotlib.pyplot as plt 
import networkx as nx

G = nx.Graph()

for i in range(0,9):
    G.add_node(i)

G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(1,4)
G.add_edge(0,3)
G.add_edge(1,5)
G.add_edge(2,5)
G.add_edge(0,4)
G.add_edge(5,4)
G.add_edge(2,7)
G.add_edge(4,8)
G.add_edge(1,8)
G.add_edge(0,7)
G.add_edge(3,7)
G.add_edge(3,6)


# person generator
def age_generator():
    age = np.random.randint(10, 100)
    return age

def gender_generator():
    gender = np.random.choice(['M', 'F'])
    return gender

def time_generator():
    time = np.random.randint(0, 100)
    return time

def get_path(G):
    
    iniz = 0
    fine = 1
    current = iniz
    lista_sensors = [iniz]

    while current != fine:
        l = [edge  for edge in list(G.edges(iniz)) if edge[1] != iniz ]

        current = l[randint(0,len(l)-1)][1]
        lista_sensors.append(current)
    


    return lista_sensors

def get_receipt():
    nmax = np.random.randint(1,20)
    products = []
    for i in range(nmax):
     products.append(np.random.randint(1,100))
    return products

#%%


def simulator(oggi, timespan, n_users):
    customers = []
    sensors = []
    receipts = []
    print(oggi)


    for i in range(n_users):
        
        offset = np.random.randint(0, timespan)
        now = oggi + datetime.timedelta(seconds=offset)
        address = np.random.randint(100000, 999999)
        customers.append({ 'time': now, 'age': age_generator(), 'gender': gender_generator(),  'address': address})
        sensor = 0
        sensors.append({ 'time': now, 'sensor':sensor , 'address': address}) # entrata 

        p = get_path(G)

        while len(p) > 0:
            now = now + datetime.timedelta(seconds=1)

            if np.random.randint(0, 10) > 5:
                sensor = p.pop(0)

            sensors.append({ 'time': now, 'sensor':sensor , 'address': address}) # entrata 
    
                
        receipts.append({ 'time': now, 'address': address, 'receipt': get_receipt()}) # entrata
                


    customers = pd.DataFrame(customers)
    sensors = pd.DataFrame(sensors).astype({'time': 'datetime64[ns]'})
    receipts = pd.DataFrame(receipts).astype({'time': 'datetime64[ns]'})
    return customers, sensors, receipts

    



        

#set max lines to see 
pd.set_option('display.max_rows', 1000)





#%%





#%%

# %%
