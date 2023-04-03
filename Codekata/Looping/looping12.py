a = input().split();
max_len = 0;
for i in a:
    if len(i) > max_len:
        max_len = len(i);

for i in range(len(a)):
    if len(a[i])<max_len:
        c = '';
        for j in range(max_len-len(a[i])):
            c = c + '0';
        a[i] = c+a[i];

final_op = '';
for i in range(0,max_len):
    sum = 0;
    for j in a:
        sum+=int(j[i]);
    ssum = str(sum);
    final_op+=ssum[len(ssum)-1];
print(final_op);
