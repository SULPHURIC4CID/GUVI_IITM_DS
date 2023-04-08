a,b = input().split();
flag = 0;
for i in a:
    if i in b:
        print('yes');
        flag = 1;
        break;
if flag == 0:
    print('no');
