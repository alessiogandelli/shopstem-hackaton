#%%
from generator import simulator
import datetime 

today = datetime.datetime(2022, 11, 11, 10, 0, 0, 0) # start date and time 11-11-21 10:00:00
timespan = 5 * 60 # number of seconds we want to generate data for
n_users = 10 # number of users we want to generate data for


customers, sensors = simulator(today, timespan, n_users)
# %%

class Person:

    def __init__(self, age, gender,  address):
        self.age = age
        self.gender = gender
        self.address = address
        self.sensors_time = self.get_sensors()

    
    def get_sensors(self):

        s = sensors[sensors['address'] == self.address].sort_values('time')


        current_sensor = 0
        start_time = min(s['time'])

        sensors_time = []

        for i, sensor in s.iterrows():
            time = sensor['time']

            if current_sensor != sensor['sensor']:
                
                delta_time = time - start_time
                sensors_time.append({'sensor': current_sensor, 'time': delta_time})
                start_time = sensor['time']

            current_sensor = sensor['sensor']

        return sensors_time
        

    
    


# %%
pippo = Person(10, 'M', 790853)
# %%
