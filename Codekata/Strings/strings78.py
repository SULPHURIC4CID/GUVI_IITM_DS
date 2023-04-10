s,k = input().split();
c=0;
for i in s:
    if i == k:
        c+=1;
if c==0:
    print('-1');
else:
    print(c);
