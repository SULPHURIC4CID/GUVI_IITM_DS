s = input();
num = ['1','2','3','4','5','6','7','8','9','0'];
alpha = ['A','B','C','D','E','F'];
power = len(s) - 1;


sum = 0;
for i in s:
    if i in num:
        sum = sum + int(i)*(16**power);
    else:
        sum = sum + (alpha.index(i.upper())+10)*(16**power);
    power-=1;
print(sum);
