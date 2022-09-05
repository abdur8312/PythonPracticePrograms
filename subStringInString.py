a = "BABAB" #"AAAAA"  "BABAB"
b = "BAB" #"AA"  "BAB"
count = 0
n = len(a)
n1 = len(b)
j = n1
for i in range(n):
    if(a[i:j] == b):
        count += 1
    j += 1
print(count)