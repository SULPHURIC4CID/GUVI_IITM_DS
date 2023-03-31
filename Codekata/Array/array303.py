n = int(input());
k = int(input());

a = [];
start = 0;
for i in range(1,n+1):
    a.append(i);
while(len(a)>1):
    dead = (start+k-1)%len(a);
    a.pop(dead);
    start = dead;
print(a[0]);

