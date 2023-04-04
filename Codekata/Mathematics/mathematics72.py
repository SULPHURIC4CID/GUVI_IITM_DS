import math

p,a  = input().split();
p = int(p);
a = int(a);
dis = (p**2/4)-4*a;
sq_dis = dis**0.5;
if sq_dis == math.ceil(sq_dis) and sq_dis == math.floor(sq_dis):
    print('yes');
else:
    print('no');
