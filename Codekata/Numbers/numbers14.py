n = input();
flag = 0;
if n[0] == '-' and len(n)>2:
    sum = int(n[1])+int(n[len(n)-1]);
    if sum%4==0:
        flag = 1;
elif len(n)>1:
    sum  = int(n[len(n)-1]) + int(n[len(n)-2]);
    if sum%4 ==0:
        flag = 1;
if flag == 1:
    print('yes');
else:
    print('no');
    
    

