s = input();
sum=0;
c='';
for i in s:
    try:
        a = int(i);
        sum = sum + a;
    except:
        c=c+i;
c=c+str(sum);
print(c);
