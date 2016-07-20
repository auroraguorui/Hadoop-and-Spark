import sys, imp
MapReduce = imp.load_source('MapReduce', '/users/aurora/box sync/data science/hadoop&spark/mapreduce/map-reduce/MapReduce.py')
 

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate((key,value),1)
    mr.emit_intermediate((value,key),1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
        total += v
    if total <2:    
        mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open('data/friends.json')
    mr.execute(inputdata, mapper, reducer)
