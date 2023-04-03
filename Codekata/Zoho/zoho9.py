def next(array):
    if len(array) < len(s):
        for j in range(len(s)):
            if j not in array:
                array.append(j);
                next(array);
    else:
        final_matrix.append(array);
        array.pop();
        
    
s = input();
num = range(len(s));
final_matrix = [];
temp = [];
for i in range(len(s)):
    temp.append(i) ;
    next(temp);

    
