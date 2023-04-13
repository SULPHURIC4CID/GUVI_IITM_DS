a = input().split();
s='';
for i in a:
    s=s+i+' ';
s = s[:len(s)-1];
d = [];
c = [];
for i in s:
    #print(i);
    if i not in d:
        d.append(i);
        c.append(1);
    else:
        c[d.index(i)]+=1;
    #print(d);
cc = '';
for i in s:
    if c[d.index(i)] > 1:
        cc+=i.upper();
    else:
        cc+=i;
print(cc);
