a =input().split();
for i in range(1,len(a)-1):
    if a[i] == 'and':
        temp = a[i-1];
        a[i-1] = a[i+1];
        a[i+1] = temp;
print(' '.join(a));
