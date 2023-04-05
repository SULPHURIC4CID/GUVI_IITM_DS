a = input().split();
c = '';
for i in range(len(a)-1):
    if a[i].lower() in ['a','an','the']:
        c+=a[i+1]+' ';
print(c[:len(c)-1]);

    
