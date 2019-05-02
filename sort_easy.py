data=[int(x) for x in input("in the data: ").split(" ")]
sorted=[]
def a():
    for i in data:
        sorted.append(min(data))
        data[data.index(min(data))]=9999999999999999999
    


