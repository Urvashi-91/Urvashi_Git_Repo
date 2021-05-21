# Let's say you have a CSV datafile:

dataFile = """
"entry1",2,3.6
"boots",5,1.7
"slack",1,2.6
"triffid",11,-1.5
"""

# The data needs to be sorted numerically  by the second column.
# How would you go about sorting the entries and dumping the
# newly sorted data?

def process(dataFile):
    dataSet = dataFile.splitlines()
    dataSet.remove('')
    output = []
    for data in dataSet:
        output.append(data.split(",")) # ["entry1",2,3.6]
    output.sort(key=lambda x:int(x[1]))
    result = " ".join(str(data) for data in output)

    print (result)


process(dataFile)
