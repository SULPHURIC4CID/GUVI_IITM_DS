n,k = input().split();
n = int(n);
k = int(k);
a = [int(i) for i in input().split()];
if k in a:
    print(a.index(k));
elif (k-1) in a:
    print(a.index(k-1));
else:
    print(-1);
