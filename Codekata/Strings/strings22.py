a = input().split();
flag = 0;
b = [];
for i in a:
    if flag == 0:
        b.append(i.upper());
        flag = 1;
    else:
        b.append(i.lower());
        flag = 0;
print(' '.join(b));
        
