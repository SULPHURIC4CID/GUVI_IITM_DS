n = int(input());
a= [int(i) for i in input().split()];
extremum = 0;
for i in range(1,n-1):
    if a[i]<a[i-1] and a[i]<a[i+1]:
        extremum+=1;
    elif a[i]>a[i-1] and a[i]>a[i+1]:
        extremum+=1;
print(extremum);
