def second(element):
    return element[1];
def first(element):
    return element[0];

n = int(input());
a = [int(i) for i in input().split()];

distinct = [];
count = [];
for i in a:
    if i not in distinct:
        distinct.append(i);
        count.append(1);
    else:
        count[distinct.index(i)]+=1;
distinct1=  [];
count1 = [];
final = [];
for i in range(len(count)):
    for j in range(count[i]):
        distinct1.append(distinct[i]);
        count1.append(count[i]);
        final.append((distinct[i],count[i]));
#print("Count1:",count1);
#print("Distinct1:",distinct1);


final.sort(key=second);

#Sorting by Count
for i in range(n):
    for j in range(n-1-i):
        if count1[j]>count1[j+1]:
            temp_count1 = count1[j];
            count1[j] = count1[j+1];
            count1[j+1] = temp_count1;
            temp_distinct1 = distinct1[j];
            distinct1[j] = distinct1[j+1];
            distinct1[j+1] = temp_distinct1;
#print("Count1:",count1);
#print("Distinct1:",distinct1);

start = final[0][1];
temp = [];
c = '';
for i in range(len(final)):
    if i != len(final) - 1:
        if final[i][1] == start:
            temp.append(final[i]);
        else:
            temp.sort(key=first);
            for j in temp:
                c+=str(j[0]);
            temp=[];
            temp.append(final[i]);
            start = final[i][1];
    else:
        if final[i][1] == start:
            temp.append(final[i]);
            temp.sort(key=first);
            for j in temp:
                c+=str(j[0]);
        else:
            c+=str(final[i][0]);


print(' '.join(c));
        
    
    



    
        



