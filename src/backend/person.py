#%%
from generator import simulator
import datetime 
import networkx as nx
import json

# create a graph representing the store, each node is a sensor and each edge is a path between two sensors
G = nx.Graph()

G.add_node(0, name="Entrance", pos = (0,0), img = "imgs/log-in.png")
G.add_node(1, name="Pants Man", pos = (0,100), img = "imgs/pants m.png")
G.add_node(2, name="Shirt Man", pos = (0,200), img = "imgs/shirt m.png")
G.add_node(3, name="Shoes Man", pos = (0,300), img = "imgs/shoe m.png")
G.add_node(4, name="Pants Woman", pos = (100,100), img = "imgs/pants w.png")
G.add_node(5, name="Shirt Woman", pos = (100,200), img = "imgs/shirt w.png")
G.add_node(6, name="Shoes Woman", pos = (100,300), img = "imgs/shoe w.png")
G.add_node(7, name="Kids", pos = (300,300), img = "imgs/kids.png")
G.add_node(8, name="Shoes Kids", pos = (300,200), img = "imgs/shoe k.png")
G.add_node(9, name="Accessories", pos = (200,0), img = "imgs/accessories.png")
G.add_node(10, name="Exit", pos = (300,0), img = "imgs/log-out.png")


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


#simulate data 




class Person:

    def __init__(self, age, gender,  address):
        self.age = age
        self.gender = gender
        self.address = address
        self.entry_time = None
        self.exit_time = None
        self.sensors_time = self.get_sensors()
        self.receipts = self.get_receipts()

    # get the path in the store counting how many seconds the person spent in each section
    def get_sensors(self):

        s = sensors[sensors['address'] == self.address].sort_values('time')


        current_sensor = 0
        start_time = min(s['time'])
        self.entry_time = start_time

        sensors_time = []

        for i, sensor in s.iterrows():  # for each second visited by the person
            time = sensor['time']

            #new sensor
            if current_sensor != sensor['sensor']:
                
                delta_time = time - start_time
                sensors_time.append({'sensor': current_sensor, 'time': delta_time}) # add the time spent in the previous section
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
        

    
def get_grouped_data(persons):
    total_sensor_time = {} # group by sensor and sum the time spent in each section
    edge_total_score = {} # count how many walk passed through each edge

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

    return total_sensor_time, edge_total_score




#  create json for the dashboard 
def get_json(total_sensor_time, edge_total_score, filename):
    #create nodes 
    nodes = []
    for node in G.nodes(data=True):
        nodo = {}
        nodo['id'] = node[1]['name']
        nodo['x'] = node[1]['pos'][0]
        nodo['y'] = node[1]['pos'][1]
        fill = {}
        fill['src'] = node[1]['img']
        nodo['fill'] = fill

        normal = {}
        normal['height'] = total_sensor_time[node[0]].total_seconds()
        nodo['normal'] = normal
        nodes.append(nodo)

    #create edges
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


    #normalize node size
    max_node = max([node['normal']['height'] for node in nodes])
    for node in nodes:
        node['normal']['height'] = (node['normal']['height']/ max_node ) * 100

    # normalize edges width
    max_edge = max([edge['normal']['stroke']['thickness'] for edge in edges])
    for edge in edges:
        edge['normal']['stroke']['thickness'] = (edge['normal']['stroke']['thickness']/ max_edge )*10 


    graph = {}
    graph['nodes'] = nodes
    graph['edges'] = edges


    # export json 
    with open(filename, 'w') as outfile:
        json.dump(graph, outfile)
        print('json created')



# %%


today = datetime.datetime(2022, 11, 11, 10, 0, 0, 0) # start date and time 11-11-21 10:00:00
timespan = 8 * 60 * 60 # number of seconds we want to generate data for
n_users = 1000 # number of users we want to generate data for


customers, sensors, receipts = simulator(today, timespan, n_users, G)

# create person objects
persons = []
for i, person in customers.iterrows():
    persons.append(Person(person['age'], person['gender'], person['address']))

# %% get all data 
persons = []
for i, person in customers.iterrows():
    persons.append(Person(person['age'], person['gender'], person['address']))
total_sensor_time, edge_total_score = get_grouped_data(persons)
get_json(total_sensor_time, edge_total_score, 'graph_all.json')


# get data for males 
persons = []
for i, person in customers.iterrows():
    if person['gender'] == 'M':
        persons.append(Person(person['age'], person['gender'], person['address']))
total_sensor_time, edge_total_score = get_grouped_data(persons)
get_json(total_sensor_time, edge_total_score, 'graph_m.json')


# get data for females
persons = []
for i, person in customers.iterrows():
    if person['gender'] == 'F':
        persons.append(Person(person['age'], person['gender'], person['address']))
total_sensor_time, edge_total_score = get_grouped_data(persons)
get_json(total_sensor_time, edge_total_score, 'graph_f.json')


# %%
