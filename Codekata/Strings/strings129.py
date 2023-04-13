a = input();
b = input();
if len(a) < len(b):
    if a in b:
        print(b.index(a)+1);
    else:
        print(-1);
else:
    if b in a:
        print(a.index(b)+1);
    else:
        print(-1);
