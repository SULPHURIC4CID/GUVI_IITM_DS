n = int(input());
a = [int(i) for i in input().split()];

c = '';
if n%2 == 1:
    for i in range(0,n//2):
        c=c+str(a[i]);
    if a[n//2] < a[n//2+1]:
        d = c[::-1];
        c=c+str(a[n//2] + 1);
        c = c + d;
    else:
        d = c[::-1];
        c=c+str(a[n//2]);
        c = c + d;
else:
    for i in range(0,n//2-1):
        c=c+str(a[i]);
    if a[n//2-1] < a[n//2]:
        c=c+str(a[n//2-1] + 1);
        c = c + c[::-1];
    else:
        c=c+str(a[n//2-1]);
        c = c + c[::-1];
print(c);
        
        
