a = [int(i) for i in input().split()]
a.sort()
print(a)

for i in a:
    if a.count(i) > 1:
        for i in a:
            a.remove(i)
            print(i, end=' ')




