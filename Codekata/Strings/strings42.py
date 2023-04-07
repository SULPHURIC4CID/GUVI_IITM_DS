s1,s2 = input().split();
d = [];
for i in s1:
    d.append(i);
c = [];
for i in s2:
    c.append(i);
e = d.copy();
for i in range(len(d)-1,-1,-1):
    if d[i] in c:
        print(d[i]);
        e.pop(i);
if len(e) == 0:
    print(-1);
else:
    m = '';
    for i in e:
        m+=i;
    print(m);
