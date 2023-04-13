def gcd(a,b):
    if a>b:
        t = a;
        a = b;
        b = t;
    for i in range(a,0,-1):
        if b%i==0:
            return i;

        
a,b = input().split();
if gcd(len(a),len(b))==1:
    print('yes');
else:
    print('no');

