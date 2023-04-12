s = input();
d = [];
c = [];
for i in s:
    if len(d) == 0:
        d.append(i);
        c.append(1);
    else:
        if i == d[len(d)-1]:
            c[len(c)-1]+=1;
        else:
            d.append(i);
            c.append(1);
op = ''
for j in range(len(d)):
    op+=d[j]+str(c[j]);
print(op);
