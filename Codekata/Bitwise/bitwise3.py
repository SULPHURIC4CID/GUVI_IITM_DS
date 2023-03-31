n = int(input());
a = [int(i) for i in input().split()];
s = a[0];
for i in range(1,n):
    s = s | a[i];
print(s);
