a = input();
b = input();
if b in a:
    l = len(b);
    s = a.index(b);
    print(a[:s]+a[s+len(b)+1:]);
else:
    print(a);
