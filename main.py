from soie import get_all_relations
from testDBpeadia import clean
from InsertRDF import sem_graph

#Enter text here <------------------------------------------------------------------------------------------->
Text= "Police have arrested 1,000 people suspected of being part of a movement blamed for the failed 2016 coup."

Triple2 = get_all_relations(Text)
Triple1 = clean (Triple2)
print(list(Triple1)+list(Triple2))
sem_graph(tuple(Triple1))

