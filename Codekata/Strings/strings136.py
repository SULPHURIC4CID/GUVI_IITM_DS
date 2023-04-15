n = int(input());
a = input().split();
prefix = input();
count = 0;
for i in a:
    if len(a)>= len(prefix):
        if prefix == i[0:len(prefix)]:
            count+=1;
print(count);
