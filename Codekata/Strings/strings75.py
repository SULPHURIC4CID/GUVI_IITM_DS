a = input().split();
b =[];
b.append(a[0]);
for i in range(1,len(a)-1):
    b.append(a[i][::-1]);
b.append(a[len(a)-1]);
print(' '.join(b))
