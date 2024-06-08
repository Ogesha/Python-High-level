def languages_known_by_all(n, student_languages):
    from functools import reduce

    all_languages = set.intersection(*student_languages)
    at_least_one_language = set.union(*student_languages)

    return all_languages, at_least_one_language

# Пример использования:
n = 3
student_languages = [
    {'English', 'Spanish'},
    {'Spanish', 'French'},
    {'Spanish', 'German'}
]
print(languages_known_by_all(n, student_languages))  # Вывод: ({'Spanish'}, {'English', 'Spanish', 'French', 'German'})
