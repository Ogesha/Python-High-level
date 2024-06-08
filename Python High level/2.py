def count_errors(dictionary, homework):
    def is_valid(word):
        return word.lower() in dictionary

    def get_variants(word):
        return dictionary.get(word.lower(), set())

    def check_accent(word):
        accents = word.count("'")
        if accents != 1:
            return False
        variants = get_variants(word)
        if not variants:
            return accents == 1
        return word in variants

    dictionary = {k.lower(): set(v) for k, v in dictionary.items()}
    homework_words = homework.split()
    errors = 0

    for word in homework_words:
        if not check_accent(word):
            errors += 1

    return errors

# Пример использования:
dictionary = {
    'молоко': {'молок\'о'},
    'вода': {'вод\'а', 'в\'ода'},
    'река': {'рек\'а'}
}
homework = "Молок\'о в\'ода вод\'а рек\'а рек\'а"
print(count_errors(dictionary, homework))  # Вывод: 1
