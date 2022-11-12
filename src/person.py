#%%
from generator import simulator
import datetime 

today = datetime.datetime(2022, 11, 11, 10, 0, 0, 0) # start date and time 11-11-21 10:00:00
timespan = 5 * 60 # number of seconds we want to generate data for
n_users = 10 # number of users we want to generate data for


customers, sensors, receipts = simulator(today, timespan, n_users)
# %%

class Person:

    def __init__(self, age, gender,  address):
        self.age = age
        self.gender = gender
        self.address = address
        self.entry_time = None
        self.exit_time = None
        self.sensors_time = self.get_sensors()
        self.receipts = self.get_receipts()

    
    def get_sensors(self):

        s = sensors[sensors['address'] == self.address].sort_values('time')


        current_sensor = 0
        start_time = min(s['time'])
        self.entry_time = start_time

        sensors_time = []

        for i, sensor in s.iterrows():
            time = sensor['time']

            if current_sensor != sensor['sensor']:
                
                delta_time = time - start_time
                sensors_time.append({'sensor': current_sensor, 'time': delta_time})
                start_time = sensor['time']

            current_sensor = sensor['sensor']

        # aggiungo l'ultimo sensor
        delta_time = time - start_time
        sensors_time.append({'sensor': current_sensor, 'time': delta_time})
        self.exit_time = time

        return sensors_time

    def get_receipts(self):
        r = receipts[receipts['address'] == self.address].sort_values('time')
        return list(r['receipt'])[0]

    def __repr__(self) -> str:
        return str(self.address) + ' ' + str(self.age) + ' ' + self.gender
        

    
    


# %%
persons = []
for i, person in customers.iterrows():
    persons.append(Person(person['age'], person['gender'], person['address']))
# %%



# %%
