import sys, imp
MapReduce = imp.load_source('MapReduce', '/users/aurora/box sync/data science/hadoop&spark/mapreduce/map-reduce/MapReduce.py')


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents

    order_id = record[1]
    mr.emit_intermediate(order_id,record)
     
     

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    order = []
    item_list = []
    for x in list_of_values:
        if x[0] == 'order':
            order.append(x)
        else:
            item_list.append(x)
    for y in item_list:
        for x in order:
            mr.emit(x+y)        

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
