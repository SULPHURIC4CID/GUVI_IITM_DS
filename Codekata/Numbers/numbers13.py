n = int(input());
a = [int(i) for i in input().split()];
k = int(input());
if k in a:
    a.sort();
    location = a.index(k);
    if len(a)%2 == 0:
        mid = len(a)//2;
        diff = abs(mid-location);
    else:
        mid = len(a)//2;
        diff = 2*abs(mid-location);
else:
    a.append(k);
    a.sort();
    location = a.index(k);
    if len(a)%2 == 0:
        mid = len(a)//2;
        diff = abs(mid-location)+1;
    else:
        mid = len(a)//2;
        diff = 2*abs(mid-location)+1;
print(diff);
        
        
        
    
