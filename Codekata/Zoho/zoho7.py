s = input();
open_bracket = ['{','[','('];
closed_bracket = ['}',']',')'];
t = [];
flag = 0;
if len(s) % 2 == 1:
    flag = 1;
if flag == 0:
    for i in s:
        if i in open_bracket:
            t.append(i);
        if i in closed_bracket:
            if i == closed_bracket[0]:
                if t[len(t)-1] == open_bracket[0]:
                    t.pop();
                else:
                    flag = 1;
                    break;
if flag == 0:
    print('yes');
else:
    print('no');
