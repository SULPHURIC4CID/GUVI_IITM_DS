a = input();
dis = [];
c=[];
for i in a:
    if i not in dis:
        dis.append(i);
    else:
        c.append(i);
if len(c) == 0:
    print(-1);
else:
    print(' '.join(c));
