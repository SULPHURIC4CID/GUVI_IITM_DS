r,c = input().split();
r = int(r);
c = int(c);
matrix = [];
sum_row = [];
for i in range(r):
    a = [int(i) for i in input().split()];
    matrix.append(a);
    sum_row.append(sum(a));
row_index = sum_row.index(max(sum_row));
print(str(row_index)+':'+str(sum_row[row_index]));

