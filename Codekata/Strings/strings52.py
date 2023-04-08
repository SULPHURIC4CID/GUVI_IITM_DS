s = input();
d = [];
c = [];
for i in s:
    if i not in d:
        d.append(i);
    else:
        c.append(i);
c1= '';
for i in d:
    if i not in c:
        c1=c1+i+' ';
print(c1[:len(c1)-1]);
                
    
