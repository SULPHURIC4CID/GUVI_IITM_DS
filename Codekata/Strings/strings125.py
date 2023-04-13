a = input();
b = input();
s = a+b;
d = []
c=[];
for i in s:
    if i not in d:
        d.append(i);
        c.append(1);
    else:
        c[d.index(i)]+=1;
if len(d) == 26 and sum(c) == 26:
    print('yes');
else:
    print('no');
    
