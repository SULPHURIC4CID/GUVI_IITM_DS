a,n = input().split();
n = int(n);
for i in a:
    val = ord(i)+n;
    if val > 122 and ord(i) > 96 and ord(i) < 123:
        val-=26;
    elif val > 90 and ord(i) > 65 and ord(i) < 91:
        val-=26;
    print(chr(val),end='');

    
