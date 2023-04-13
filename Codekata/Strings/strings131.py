a = input();
c = '';
for i in range(1,len(a),2):
    if int(a[i]) % 2 == 1:
        c=c+a[i-1]+a[i];
    else:
        for j in range(int(a[i])):
            c+=a[i-1];
print(c);
