def is_palindrome(a):
    if a == a[::-1]:
        return True;
    else:
        return False;
    
a,b = input().split();
dis1 = [];
c1 = [];
for i in a:
    if i not in dis1:
        dis1.append(i);
        c1.append(1);
    else:
        c1[dis1.index(i)]+=1;
dis2 = [];
c2 = [];
for i in b:
    if i not in dis2:
        dis2.append(i);
        c2.append(1);
    else:
        c2[dis2.index(i)]+=1;

if is_palindrome(a) and is_palindrome(b):
    if dis1==dis2 and c1==c2:
        print(1);
    else:
        print(0);
else:
    print(0);
