def common_colors(set1, set2):
    return len(set1 & set2)

def all_colors(set1, set2):
    return len(set1 | set2)

# Пример использования:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(common_colors(set1, set2))  # Вывод: 2
print(all_colors(set1, set2))  # Вывод: 8
