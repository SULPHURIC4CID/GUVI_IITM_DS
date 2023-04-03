s = input();
roman = ['C','L','X','V','I'];
special = ['XC','XL','IX','IV'];
flag = 1;
for i in s:
    if i not in roman:
        flag = 0;
        print(-1);
        break;

#Splitting roman string
if flag == 1:
    group = [];
    temp = '';
    for i in range(0,len(s)):
        if roman.index(s[i])<roman.index(s[i-1]) and i != 0:
            temp=temp+s[i];
            group.pop();
            group.append(temp);
            #print(temp,group);
            temp = '';
        else:
            temp = s[i];
            group.append(temp);
            #print(temp,group);
    sum = 0;
    for i in group:
        if i == 'I':
            sum+=1;
        elif i == 'V':
            sum+=5;
        elif i == 'X':
            sum+=10;
        elif i == 'L':
            sum+=50;
        elif i == 'C':
            sum+=100;
        elif i == 'XC':
            sum+=90;
        elif i == 'XL':
            sum+=40;
        elif i == 'IX':
            sum+=9;
        elif i == 'IV':
            sum+=4;
    print(sum);
        
        


                   
    
        
    
