a = input().split();

op = '';
for i in a:
    for j in range(len(i)):
        if j == 0:
            op+=i[j].upper();
        else:
            op+=i[j].lower();
print(op);
