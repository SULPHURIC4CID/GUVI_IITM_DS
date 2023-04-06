a = input().split();
cons = ['a','e','i','o','u'];
c='';
for i in a:
    for j in i:
        if j.lower() not in cons:
            c=c+j;
    c=c+' ';
print(c[:len(c)-1]);

    
     
