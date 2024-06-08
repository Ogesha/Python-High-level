def find_synonym(synonyms, word):
    synonym_dict = {}
    for word1, word2 in synonyms:
        synonym_dict[word1] = word2
        synonym_dict[word2] = word1

    return synonym_dict.get(word, None)

# Пример использования:
synonyms = [('hello', 'hi'), ('bye', 'goodbye')]
word = 'hello'
print(find_synonym(synonyms, word))  # Вывод: 'hi'
