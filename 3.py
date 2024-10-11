#Первое задание на множества, словари
#Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите
#слово YES (в #отдельной строке), если это число ранее встречалось в последовательности или NO
#если не встречалось.

input_data = list(map(int, input().split()))
used_digits = []

for digit in input_data:
	if digit not in used_digits:
		print("NO")
	else:
		print("YES")
	used_digits.append(digit)