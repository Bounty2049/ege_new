f = open('9.txt')
count = 0
for s in f:
    m = [int(x) for x in s.split()]
    p = [int(x) for x in m if m.count(x)>1]
    n = [int(x) for x in m if m.count(x)==1]
    if len(p)>0 and len(n)>0:
        if sum(n)/len(n) < sum(p)/len(p):
            count += 1
print(count)