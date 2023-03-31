n = int(input());
a = [int(i) for i in input().split()];
a1 = a[0::2];
a2 = a[1::2];
a1.sort();
b = [];
for i in range(len(a1)):
    b.append(str(a1[i]));
    try:
        b.append(str(a2[i]));
    except:
        continue;
print(' '.join(b));
