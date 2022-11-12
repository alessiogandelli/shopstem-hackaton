#%%
from generator import simulator
import datetime 
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


today = datetime.datetime(2022, 11, 11, 10, 0, 0, 0) # start date and time 11-11-21 10:00:00
timespan = 8 * 60 * 60 # number of seconds we want to generate data for
n_users = 1000 # number of users we want to generate data for



customers, sensors, receipts = simulator(today, timespan, n_users, G)
# %%
customers.join(sensors, on='address', how='left').join(receipts, on='address', how='left')


# drop column time 
customers = customers.drop(columns=['time'])
customers.set_index('address', inplace=True)
sensors.set_index('address', inplace=True)




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
        

    def get_df(self):
        returnc
    
    


# %%
persons = []
for i, person in customers.iterrows():
    persons.append(Person(person['age'], person['gender'], person['address']))
# %%



# %%
