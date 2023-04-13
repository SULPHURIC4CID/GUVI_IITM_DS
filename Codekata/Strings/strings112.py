def fact(a):
    mul = 1;
    for i in range(1,a+1):
        mul*=i;
    return mul;
    

a,b = input().split();
a = int(a);
b = int(b);
if a<b:
    print(fact(a));
else:
    print(fact(b));
