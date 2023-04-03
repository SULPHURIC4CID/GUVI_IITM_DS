n = input();
a = [int(i) for i in input().split()];
def divide(a):
    if a%i == 0:
        return a//i;        
    else:
        return a;

max_val = max(a);
b = a.copy();
lcm = 1;
while(sum(b) > len(a)):
    for i in range(2,max_val+1):
        sum_ini = sum(b);
        b = list(map(divide,b));
        sum_final = sum(b);
        if sum_ini != sum_final:
            lcm = lcm * i;
            break;
print(lcm);
