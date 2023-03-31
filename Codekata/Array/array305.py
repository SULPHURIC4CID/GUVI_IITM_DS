n = int(input());
a = [int(i) for i in input().split()];
marks = [int(i) for i in input().split()];
b = a.copy();
count = [0]*n;
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            temp = a[j];
            a[j] = a[j+1];
            a[j+1] = temp;
            count[a[j]-1]+=1;
            count[a[j+1]-1]+=1;
            #marks[b.index(a[j])]-=1;
            #marks[b.index(a[j+1])]-=1;

marks = list(map(lambda x,y: x-y,marks,count));
c= '';
for i in marks:
    c=c+str(i)+' ';
print(c[:len(c)-1]);

