#%%

import time
import numpy as np
import pandas as pd
import datetime

# age generator 
def age_generator():
    age = np.random.randint(10, 100)
    return age

def gender_generator():
    gender = np.random.choice(['M', 'F'])
    return gender

def time_generator():
    time = np.random.randint(0, 100)
    return time




customers = []
sensors = []
for i in range(10):
    now = datetime.datetime.now()
    customers.append({ 'time': now, 'age': age_generator(), 'gender': gender_generator()})

    



   # sensors.append({ 'time': now, 'id' : 0 , 'power': time_generator() })

pd.DataFrame(customers)
    



        






# %%
