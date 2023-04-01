def is_palindrome(s):
    if s == s[::-1]:
        return True;
    else:
        return False;
        
s = input();
substring = [];
flag = 0;
for i in range(len(s)):
    for j in range(i,len(s)):
        substring.append(s[i:j+1]);
max_len = 0;

for i in substring:
    if is_palindrome(i):
        if len(i) > max_len:
            max_len = len(i);
            max_word = i;
print(max_word);

        
