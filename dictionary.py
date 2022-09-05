def convert_to_Dict(numbers):
    dict1 = {}
    for i in numbers:
        if dict1.get(i) is None:
            dict1[i] = 1
        else:
            dict1[i] = dict1.get(i) + 1
    return dict1

def getValues_ofDict(dict1, numbers):
    values = []
    uniq_numbers = list(set(numbers))
    for j in uniq_numbers:
        c = dict1.get(j)
        values.append(c)
    return values

def Sort(values):
    n = len(values)
    for i in range(n-1):
        i = 0
        for j in range(1, n):
            if(values[i] > values[j]):
                values[i], values[j] = values[j], values[i]
                i += 1
            else:
                i += 1
    return values

a = [5,5,5,4,3,3,4,3,5,4,6,3]
a_Dict = convert_to_Dict(a)
print(a_Dict)
b = getValues_ofDict(a_Dict, a)
c = Sort(b)
print(c)