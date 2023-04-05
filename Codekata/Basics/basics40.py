a,b = input().split();

if (a=='R' and b =='P') or (a=='P' and b=='R'):
    print('P');
elif (a=='R' and b =='S') or (a=='S' and b=='R'):
    print('R');
elif a==b:
    print('D');
else:
    print('S');
    
