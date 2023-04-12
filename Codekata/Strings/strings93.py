a = input().split();
max_len = 0;
for i in a:
    if len(i)>max_len:
        d = i;
        max_len = len(i);
print(d);
