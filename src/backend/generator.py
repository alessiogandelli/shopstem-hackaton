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




# random age 10 to 100
def age_generator():
    age = np.random.randint(10, 100)
    return age

#get a random gender
def gender_generator():
    gender = np.random.choice(['M', 'F'])
    return gender


def time_generator():
    time = np.random.randint(0, 100)
    return time

# create a random path from start to end
def get_path(G):
    
    iniz = 0
    fine = 10
    current = iniz
    lista_sensors = [iniz]

    while current != fine:
        l = [edge  for edge in list(G.edges(current)) if edge[1] != current ]

        current = l[randint(0,len(l)-1)][1]

        lista_sensors.append(current)
    


    return lista_sensors

# get a random receipt
def get_receipt():
    nmax = np.random.randint(1,20)
    products = []
    for i in range(nmax):
     products.append(np.random.randint(1,100))
    return products

#%%

# create three tables to simulate, custumers entering the store, the sensors and the receipts
def simulator(oggi, timespan, n_users, G):
    customers = []
    sensors = []
    receipts = []

    #generate n customers
    for i in range(n_users):
        
        offset = np.random.randint(0, timespan) # random offset from the start time
        now = oggi + datetime.timedelta(seconds=offset) 
        address = np.random.randint(100000, 999999) # random address
        customers.append({ 'time': now, 'age': age_generator(), 'gender': gender_generator(),  'address': address})
        sensor = 0
        sensors.append({ 'time': now, 'sensor':sensor , 'address': address}) # entrata 

        p = get_path(G)

        while len(p) > 0:
            now = now + datetime.timedelta(seconds=1)

            if np.random.randint(0, 100) > 80:
                sensor = p.pop(0)

            sensors.append({ 'time': now, 'sensor':sensor , 'address': address}) # entrata 
    
                
        receipts.append({ 'time': now, 'address': address, 'receipt': get_receipt()}) # entrata
                


    customers = pd.DataFrame(customers)
    sensors = pd.DataFrame(sensors).astype({'time': 'datetime64[ns]'})
    receipts = pd.DataFrame(receipts).astype({'time': 'datetime64[ns]'})
    return customers, sensors, receipts

    



        



