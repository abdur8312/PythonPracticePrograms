def findArmstrong(a):
    result = 0
    list_a = list(str(a))
    n = len(list_a)
    for i in list_a:
        result += int(i) ** n
    if(a == result):
        print(a,"is a armstrong number")
a = 1
b = 55000
for i in range(a,b):
    findArmstrong(i)
    