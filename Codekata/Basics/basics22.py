n = int(input());
a = [int(i) for i in input().split()];

sum = a[0];
for i in range(1,len(a)):
    sum = sum & a[i];
print(sum);
    
