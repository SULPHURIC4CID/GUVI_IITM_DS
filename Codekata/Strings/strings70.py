n,m = input().split();
n = int(n);
m = int(m);
flag = 0;
for i in range(n):
    a,b = input().split();
    a = int(a);
    b = int(b);
    if m>= a and m<= b:
        flag = 1;
        break;
if flag == 1:
    print('yes');
else:
    print('no');
