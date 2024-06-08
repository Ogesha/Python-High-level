def possible_numbers(n, questions):
    possible = set(range(1, n + 1))

    for question, answer in questions:
        question_set = set(question)
        if answer == 'YES':
            possible &= question_set
        else:
            possible -= question_set

    return possible

# Пример использования:
n = 10
questions = [
    ([1, 2, 3], 'NO'),
    ([2, 4, 6, 8, 10], 'YES'),
    ([1, 2, 10], 'NO')
]
print(possible_numbers(n, questions))  # Вывод: {4, 6, 8}
