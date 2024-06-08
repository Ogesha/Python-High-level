def calculate_strike_days(N, K, parties):
    strike_days = set()

    for party in parties:
        a, b = party
        day = a
        while day <= N:
            if day % 7 not in (6, 0):  # 6 и 0 - это суббота и воскресенье
                strike_days.add(day)
            day += b

    return len(strike_days)

# Пример использования:
N = 10
K = 2
parties = [(3, 2), (5, 3)]
print(calculate_strike_days(N, K, parties))  # Вывод: 5
