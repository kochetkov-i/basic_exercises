# Вывести последнюю букву в слове
print("Вывести последнюю букву в слове")
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
lower_word = word.lower()
print("Вывести количество букв 'а' в слове")
print(lower_word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
vowels_in_word = 0
lower_word = word.lower()
for char in lower_word:
    if char in vowels:
        vowels_in_word += 1
print("Вывести количество гласных букв в слове")
print(vowels_in_word)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print("Вывести количество слов в предложении")
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
avg_word_len = len(sentence.replace(' ','')) /len(words)
print("Вывести усреднённую длину слова в предложении")
print(int(avg_word_len))