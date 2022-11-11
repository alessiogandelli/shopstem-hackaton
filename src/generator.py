#%%

import time
import numpy as np
import pandas as pd
import datetime



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

def get_path():
    return [0,1,3,2,3,4,0]


customers = []
sensors = []

today = datetime.datetime(2022, 11, 11, 10, 0, 0, 0) # start date and time 11-11-21 10:00:00
timespan = 5 * 60 # number of seconds we want to generate data for
n_users = 10 # number of users we want to generate data for


for i in range(n_users):
    offset = np.random.randint(0, timespan)
    now = today + datetime.timedelta(seconds=offset)
    customers.append({ 'time': now, 'age': age_generator(), 'gender': gender_generator()})
    address = np.random.randint(100000, 999999)

    p = get_path()

    while len(p) > 0:
        now = now + datetime.timedelta(seconds=1)
        if np.random.randint(0, 10) > 7:
            sensor = p.pop(0)
            

        sensors.append({ 'time': now, 'sensor':sensor , 'address': address})

    for sensor in p:
        wait = np.random.randint(0, 100)
        now = now + datetime.timedelta(seconds=wait)
        sensors.append({'time': now , 'sensor_id': sensor})




pd.DataFrame(customers)
sensors = pd.DataFrame(sensors).astype({'time': 'datetime64[ns]'})

    



        

#set max lines to see 
pd.set_option('display.max_rows', 1000)




# %%
