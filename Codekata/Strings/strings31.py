a = input().split();
dis = [];
count = [];
for i in a:
    if i not in dis:
        dis.append(i);
        count.append(1);
    else:
        count[dis.index(i)]+=1;
maxc = max(count);
b = [];
for i in range(len(count)):
    if count[i] == maxc:
       b.append(dis[i]);
b.sort();
print(b[0],maxc);
    
