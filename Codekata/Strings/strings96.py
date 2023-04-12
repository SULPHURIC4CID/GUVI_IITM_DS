s = input();
cc = 0;
for i in s:
    if i != 'a' and i != 'b':
        cc+=1;
if cc == 0:
    print('yes');
else:
    print('no');
