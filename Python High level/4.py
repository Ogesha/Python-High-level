def count_word_occurrences(filename):
    with open(filename, 'r') as file:
        words = file.read().split()

    word_count = {}
    occurrences = []

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        occurrences.append(word_count[word] - 1)

    return occurrences


# Пример использования:
filename = "input.txt"
# Пример содержимого файла: "hello world hello"
print(count_word_occurrences(filename))  # Вывод: [0, 0, 1]
