#Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой

input_data = list(map(int, input().split()))
rows, cols = input_data[0], input_data[1]
array = [[0]* cols for _ in range(rows)]
snake_counter = 0

for row in range(rows):
	if row%2:
		for col in range(cols):
			array[row][col] = snake_counter
			snake_counter+=1
			print(array[row][col],end = '\t')
	else:
		for col in range(cols-1,-1,-1):
			array[row][col] = snake_counter
			snake_counter+=1
			print(array[row][col],end = '\t')
	print()