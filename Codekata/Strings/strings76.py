s = input();
c='';
for i in s:
    if i.lower() == i:
        c+=i.upper();
    else:
        c+=i.lower();
print(c);
