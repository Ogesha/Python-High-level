from collections import Counter
import re

def sort_words_by_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words

# Пример использования:
text = "hello world hello"
print(sort_words_by_frequency(text))  # Вывод: [('hello', 2), ('world', 1)]
