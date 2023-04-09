# What is a graph? A graph it is a connection set. Every graph it is constituted of nodes and edges. A node can be directly connected to edges.

# We're going to use graph data structure in the algorithm called breadth-first search.
# The algorithm breadth-first search only works if we search for the data in the order they are added, so to do this we need to use the QUEUE data structure.

# We're going to apply the algorithm above using the idea of a mango seller, so we need to discover if the last letter of the person name's is 'm' to be a mango seller,
# if not continue looking.

# The breadth-first search algorithm has the thinking to while it finding the path to get the mango seller, looks for the smallest path to find it.

from collections import deque

graph = {}
graph ["you"] = ["alice", "bob", "claire"]
graph ["bob"] = ["anuj","peggy"]
graph ["alice"] = ["peggy"]
graph ["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue = graph["you"]
    person_checked = []
    while search_queue:
        person = search_queue.pop(0)
        if not person in person_checked:
            if person_is_seller(person):
                print(person + " is mango a seller")
                return True
            else:
                print("No mango seller")
                search_queue += graph[person]
                person_checked.append(person)
    return False

print(search(graph["you"]))




