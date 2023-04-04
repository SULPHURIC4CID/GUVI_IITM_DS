a,d,n = input().split();
a = int(a);
d = int(d);
n = int(n);
val = a;
sum = a;
itr = 1;
while (itr < n):
    val=val+d;
    sum+=val;
    itr+=1;
print(sum);
