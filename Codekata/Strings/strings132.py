s = input();
d = [];
c = [];
for i in s:
    if i not in d:
        d.append(i);
        c.append(1);
    else:
        c[d.index(i)]+=1;
#print(c);
#print(d);
for i in range(len(c)):
    for j in range(len(c)-1):
        if c[j]>c[j+1]:
            t = c[j];
            c[j] = c[j+1];
            c[j+1] = t;
            t = d[j];
            d[j] = d[j+1];
            d[j+1] = t;
#print(c);
#print(d);
cc = '';
for i in range(len(d)):
    for j in range(c[i]):
        cc+=d[i];
print(cc);
            
        
