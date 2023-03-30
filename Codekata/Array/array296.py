n,k = input().split();
n = int(n);
k = int(k);
a = [int(i) for i in input().split()];
price_charged = int(input());
key = [1]*n;
key[k] = 0;
result = list(map(lambda x,y:x*y,a,key));
actual = sum(result)//2;
if actual == price_charged:
    print('Bon Appetit');
else:
    print(price_charged-actual);
