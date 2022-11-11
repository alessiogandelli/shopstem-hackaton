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

def get_path():
    return [0,1,3,2,3,4,0]


customers = []
sensors = []
for i in range(1):
    now = datetime.datetime.now()
    customers.append({ 'time': now, 'age': age_generator(), 'gender': gender_generator()})
    

    p = get_path()

    while len(p) > 0:
        now = now + datetime.timedelta(seconds=1)
        if np.random.randint(0, 10) > 5:
            sensor = p.pop(0)
            print('sensor', sensor)

        sensors.append({ 'time': now, 'sensor':sensor })

    for sensor in p:
        wait = np.random.randint(0, 100)
        now = now + datetime.timedelta(seconds=wait)
        sensors.append({'time': now , 'sensor_id': sensor})




pd.DataFrame(customers)
pd.DataFrame(sensors)
    



        






# %%
