def find_coins_greedy(amount, coins):
    # Сортуємо монети у спадному порядку
    coins.sort(reverse=True)
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result


def find_min_coins(amount, coins):
    # Ініціалізуємо таблицю для динамічного програмування
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [0] * (amount + 1)
    result = {coin: 0 for coin in coins}

    # Проходимося по всім монетам і оновлюємо dp
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_count[x] = coin

    # Відтворюємо кількість монет для оптимального розв'язку
    x = amount
    while x > 0:
        coin = coin_count[x]
        result[coin] += 1
        x -= coin

    # Видаляємо нулі з результату
    result = {k: v for k, v in result.items() if v > 0}

    return result


# Приклад використання
coins = [50, 25, 10, 5, 2, 1]
amount = 113

print("Жадібний алгоритм:", find_coins_greedy(amount, coins))
print("Алгоритм динамічного програмування:", find_min_coins(amount, coins))