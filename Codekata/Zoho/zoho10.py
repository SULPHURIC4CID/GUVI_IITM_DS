s = input().split();
t1 = [];
for i in s:
    t1.append(i);
t2 = [];
for i in range(len(s)):
    t2.append(t1.pop());
print(' '.join(t2));

    
