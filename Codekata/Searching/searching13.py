def num_remaining(n,k):
    temp = list(range(1,n+1));
    #print(temp);
    while(len(temp)>=k):
        for i in range(len(temp)-1,-1,-1):
            if ((i+1)%k) != 0:
                temp.pop(i);
        #print(temp);
    temp.sort();
    return temp[0];

t = int(input());
for i in range(t):
    a,b = input().split();
    print(num_remaining(int(a),int(b)));

    
        
