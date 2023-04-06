a = input();
count=0;
for i in range(0,5):
    if ord(a[i].upper()) in list(range(65,91)):
        count+=1;
num = [1,2,3,4,5,6,7,8,9,0];
try:
    for i in range(5,9):
        if int(a[i]) in num:
            count+=1;
    if ord(a[9].upper()) in list(range(65,91)):
        count+=1;
except:
    count=0;
if count==10:
    print('pan');
else:
    print('not pan');
