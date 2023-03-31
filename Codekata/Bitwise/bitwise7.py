n = int(input());
a = [int(i) for i in input().split()];
c = a[0];
for i in range(1,n):
    c = c ^ ((c ^ a[i]) & -(c < a[i]))
print(c);
