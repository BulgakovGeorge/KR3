#Дан массив N × M. Требуется повернуть его по часовой стрелке на 90 градусов

input_data = list(map(int, input().split()))
rows, cols = input_data[0], input_data[1]
table = []
for _ in range(rows):
    table.append(list(map(int, input().split())))
print(cols, rows)
for col in range(cols):
    for row in range(rows-1, -1, -1):
        print(table[row][col], end='\t')
    print()
