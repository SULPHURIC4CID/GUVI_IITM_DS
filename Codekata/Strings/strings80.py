s = input().split();
d = [];
c = [];
for j in s:
    for i in j:
        if i not in d:
            d.append(i);
            c.append(1);
        else:
            c[d.index(i)]+=1;
e = [];
for i in range(len(c)):
    if c[i] == min(c):
        e.append(d[i]);
print(''.join(e))
    
