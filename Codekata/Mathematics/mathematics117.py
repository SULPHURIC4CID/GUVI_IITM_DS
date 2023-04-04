def is_prime(a):
    if a==1:
        return False;
    c = 0;
    for i in range(2,a):
        if a%i==0:
            c+=1;
    if c==0:
        return True;
    else:
        return False;
        
n = int(input());

prime_fac = [];
for i in range(1,n+1):
    if n%i==0 and is_prime(i) and is_prime(n//i):
        temp = [str(i),str(n//i)];
        temp.sort();
        if temp not in prime_fac:
            prime_fac.append(temp);
if len(prime_fac) == 0:
    print(-1);
else:
    for i in prime_fac:
        print(' '.join(i));
        
        
        
