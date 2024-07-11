f = open("9.txt", 'r', encoding='utf-8')
cnt = 0

for i in f:
    l = sorted(int(x) for x in i.split())
    if len(set(l)) == 4 and (sum(l) / len(l) > (sum(l) - sum(set(l))) - len(set(l))):
        cnt += 1

print(cnt)
# x = [1, 1, 1, 1, 5, 2, 8]
# print(len(x))
# print(len(set(x)))
# print(set(x))

# Incorrect solving