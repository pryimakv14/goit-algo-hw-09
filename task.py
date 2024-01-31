from collections import Counter


def max_coins_dynamic(amount, coins):
    K = [float('inf')] * (amount + 1)
    K[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            K[i] = min(K[i], K[i - coin] + 1)

    result = []
    remaining_amount = amount
    while remaining_amount > 0:
        for coin in coins:
            if remaining_amount >= coin and K[remaining_amount - coin] == K[remaining_amount] - 1:
                result.append(coin)
                remaining_amount -= coin
                break

    return dict(Counter(result))


def max_coins_greedy(amount, coins):
    coins.sort(reverse=True)
    result = []
    remaining_amount = amount
    while remaining_amount > 0:
        for coin in coins:
            if remaining_amount >= coin:
                result.append(coin)
                remaining_amount -= coin
                break

    return dict(Counter(result))


coins = [25, 10, 50, 5, 2, 1]
amount = 113
max_coins_list_dynamic = max_coins_greedy(amount, coins)
print(f"The maximum amount of coins for {amount} is: {max_coins_list_dynamic} - Greedy Approach")
max_coins_list_dynamic = max_coins_dynamic(amount, coins)
print(f"The maximum amount of coins for {amount} is: {max_coins_list_dynamic} - Dynamic Programming Approach")


coins = [50, 40, 25, 10, 5, 2, 1]
amount = 80
max_coins_list_dynamic = max_coins_greedy(amount, coins)
print(f"The maximum amount of coins for {amount} is: {max_coins_list_dynamic} - Greedy Approach 2")
max_coins_list_dynamic = max_coins_dynamic(amount, coins)
print(f"The maximum amount of coins for {amount} is: {max_coins_list_dynamic} - Dynamic Programming Approach 2")
