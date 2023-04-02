# What is Hash Tables? 

# With Hash tables are possible to map key values.

# Hash tables implements an array under the hood, and the hash function is responsible to map the key with the value. 

# After the hash function do the map, it gives us an index, this index is responsible to show us where the map is stored in the array.

# In summary, hash tables are good with:
# the relation between two itens; 
# filter for duplicates;
# caching/memorization of data, instead of requesting this data from the server.

# A good hash function distributes the values ​​in the array symmetrically, avoiding collision (it is when two keys are indicated in the same space (index) of an array)

voted = {}

def check_vote(name):
    if voted.get(name):
        print(name + " Go away you already voted")
    else:
        voted[name] = True
        print(name + " Can vote")
    
check_vote("noah")

check_vote("pedro")

check_vote("gustavo")

check_vote("noah")
