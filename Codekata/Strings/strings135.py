s = input();
flag = 1;
for i in range(len(s)):
    for j in s[i+1:]:
        if ord(j)>ord(s[i]):
            flag=0;
            val = i;
            break;
    if flag==0:
        break;
if flag==0:
    print('Possible');
    
else:
    print('Impossible');
    
