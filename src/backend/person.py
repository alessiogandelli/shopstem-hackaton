#%%
from generator import simulator
import datetime 
import networkx as nx

G = nx.Graph()

G.add_node(0, name="Entrance", pos = (0,0))
G.add_node(1, name="Pants Man", pos = (0,100))
G.add_node(2, name="Shirt Man", pos = (0,200))
G.add_node(3, name="Shoes Man", pos = (0,300))
G.add_node(4, name="Pants Woman", pos = (100,100))
G.add_node(5, name="Shirt Woman", pos = (100,200))
G.add_node(6, name="Shoes Woman", pos = (100,300))
G.add_node(7, name="Kids", pos = (300,300))
G.add_node(8, name="Shoes Kids", pos = (300,200))
G.add_node(9, name="Accessories", pos = (200,0))
G.add_node(10, name="Exit", pos = (300,0))


G.add_edge(0,1)
G.add_edge(0,9)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,6)
G.add_edge(9,4)
G.add_edge(1,9)
G.add_edge(4,5)
G.add_edge(5,6)
G.add_edge(5,7)
G.add_edge(5,8)
G.add_edge(6,7)
G.add_edge(6,8)
G.add_edge(7,8)
G.add_edge(8,10)

#draw
nx.draw(G, with_labels=True, font_weight='bold')


today = datetime.datetime(2022, 11, 11, 10, 0, 0, 0) # start date and time 11-11-21 10:00:00
timespan = 8 * 60 * 60 # number of seconds we want to generate data for
n_users = 1000 # number of users we want to generate data for



customers, sensors, receipts = simulator(today, timespan, n_users, G)
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

total_sensor_time = {}
edge_total_score = {}

for person in persons:
    sensor_time = person.sensors_time
    current = None
    for sen in sensor_time:

        if current != None:
            edge = (min(current, sen['sensor']), max(current, sen['sensor']))
            current = sen['sensor']
            if edge in edge_total_score:
                edge_total_score[edge] += 1
            else:
                edge_total_score[edge] = 1
        else:
            current = sen['sensor']
        

        if sen['sensor'] in total_sensor_time:
            total_sensor_time[sen['sensor']] += sen['time']
        else:
            total_sensor_time[sen['sensor']] = sen['time']



#%%


nodes = []


for node in G.nodes(data=True):
    nodo = {}
    nodo['id'] = node[1]['name']
    nodo['x'] = node[1]['pos'][0]
    nodo['y'] = node[1]['pos'][1]
    normal = {}
    normal['height'] = total_sensor_time[node[0]].total_seconds()
    nodo['normal'] = normal
    nodes.append(nodo)

#%%
edges = []

for edge in G.edges():
    arco = {}
    arco['from'] = G.nodes[edge[0]]['name']
    arco['to'] = G.nodes[edge[1]]['name']
    normal = {}
    stroke = {}
    stroke['thickness'] = edge_total_score[edge] 
    normal['stroke'] = stroke
    arco['normal'] = normal
    edges.append(arco)

# %%



max_node = max([node['normal']['height'] for node in nodes])
for node in nodes:
    node['normal']['height'] = (node['normal']['height']/ max_node ) * 10


max_edge = max([edge['normal']['stroke']['thickness'] for edge in edges])
for edge in edges:
    edge['normal']['stroke']['thickness'] = (edge['normal']['stroke']['thickness']/ max_edge ) * 10


graph = {}
graph['nodes'] = nodes
graph['edges'] = edges


#%%
import json
# export json 
with open('graph.json', 'w') as outfile:
    json.dump(graph, outfile)

# %%
