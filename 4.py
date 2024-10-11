#Второе задание на множества, словари
#Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову
#Все слова в словаре различны. Для одного данного слова определите его синоним.

dictionary = {}

for _ in range(int(input())):
	input_data = list(map(str, input().split()))
	key, data = input_data[0], input_data[1]
	dictionary[key] = data
	dictionary[data] = key

find_word = input()

if dictionary.get(find_word):
	print(dictionary.get(find_word))
else:
	print("Слово не найдено") 