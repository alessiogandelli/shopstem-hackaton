# shopstems-hackaton

This is the code I submitted for the challenge at this [hackaton](https://hackathon.bz.it)



The goal of this project is to help small-medium businesses to undrstand better their customers, we help them using bluetooth and camera to track people inside the store giving them insights about the different segments of clients they have.

We decided to present to the business owner simple but effective statistics: we segmented using gender and age. Moreover using different bluetooth sensors we are able to detect where the people of the different segments stops more and thanks to the timestamp of the receipt we are able to detect the number items purchased.

The date we use is simulated, since we do not have the necessary sensors.

## generator 
we generate 3 tables:  
- customers 
- sensors 
- receipts 

The tables are generate not in a totally random way, in fact we simulated a real possible path they can do.

## dashboard 
We used anyCharts library to render interactive graphs and plots, and a simple html to merge all the data. There is still a lot to work to do here.
