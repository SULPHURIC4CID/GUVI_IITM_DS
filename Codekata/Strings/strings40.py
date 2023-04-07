s = input();
mid = len(s)//2;
if s[0].lower() == 'a' and s[mid].lower() == 'm' and s[len(s)-1].lower() == 'z':
    print(1);
else:
    print(0);
