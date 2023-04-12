a = input();
b = input();

da = [];
ca = [];
db = [];
cb = [];

for i in a:
    if i not in da:
        da.append(i);
        ca.append(1);
    else:
        ca[da.index(i)]+=1;

for i in b:
    if i not in db:
        db.append(i);
        cb.append(1);
    else:
        cb[db.index(i)]+=1;
da.sort();
ca.sort();
db.sort();
cb.sort();

if da==db and ca==cb:
    print('yes');
else:
    print('no');
    
            
