# Dijkstra algorithm it is not only used to show the minimal time to travel a path, but show how to reduce something, like
# what is the cheapest way to buy a thing that you want.

# Dijkstra algorithm works with weighted edges, so important thing to mention about this is that we assume that the edges
# are all positives, because the algorithms brokes with negative numbers. 

graph = {}
graph["start"] = {}

graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity
                                   
parent = {}
parent["a"] = "start"
parent["b"] = "start"
parent["end"] = None

processed = {}  

def find_the_lowest_cost(costs):
    lowest_cost = float("inf")
    node_with_lowest_cost = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            node_with_lowest_cost = node
    return node_with_lowest_cost 

node = find_the_lowest_cost(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if(costs[n] > new_cost):
            costs[n] = new_cost
            parent[n] = node
    processed.append(node)
    node = find_the_lowest_cost(costs)