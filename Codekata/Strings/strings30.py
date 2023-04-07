a = input();
dis = [];
c=[];
for i in a:
    if i not in dis:
        dis.append(i);
    else:
        c.append(i);
for i in a:
    if i not in c:
        print(i);
        break;
    
