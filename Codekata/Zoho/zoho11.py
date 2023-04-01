n = int(input());
a = input().split();
for i in range(n):
    a[i] = int(a[i]);

for i in range(n):
    if i == n-1:
        print(-1);
        break;
    flag = 0;
    for j in range(n):
        if j > i:
            if a[j] < a[i]:
                print(a[j],end=" ");
                flag = 1;
                break;
        else:
            continue;
    if flag == 0:
        print(-1,end=" ");
        flag = 1;
    
            
