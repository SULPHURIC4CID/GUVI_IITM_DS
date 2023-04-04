
def is_prime(a):
    count = 0;
    for i in range(1,a+1):
        if a%i==0:
            count+=1;
    if count==2:
        return True;
    else:
        return False;
        

def is_dfg(a):
    temp = [];
    for i in range(2,a+1):
        if a%i == 0 and is_prime(i):
            temp.append(i);
    cn = 0;
    print(temp);
    for i in temp:
        if i in [2,3,5]:
            cn+=1;
    if cn != 0 and cn <= 3:
        return True;
    else:
        return False;
        

n = int(input());
c=[];
c.append('1');
for j in range(2,n+1):
    if is_dfg(j):
        c.append(str(j));
print(' '.join(c));
        
