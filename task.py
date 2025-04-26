import timeit
from colorama import Fore, Style

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount) -> object:
    """
    Find the minimum number of coins needed to make a given amount of money.
    """
    coins_result = {}

    while amount > 0:
        for coin in coins:
            if amount >= coin:
                amount -= coin
                coins_result[coin] = coins_result.get(coin, 0) + 1
                break

    return coins_result


def find_min_coins(amount):
    """
    Find the minimum number of coins needed to make a given amount of money.
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)
    result = {}

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


def test_algorythm_time(algorythm, amount) -> int:
    start_time = timeit.default_timer()
    algorythm(amount)
    end_time = timeit.default_timer()
    return end_time - start_time


def test_algorythm(algorythm) -> int:
    return {
        "small_amount": test_algorythm_time(algorythm, 115),
        "medium_amount": test_algorythm_time(algorythm, 1015),
        "big_amount": test_algorythm_time(algorythm, 1000049),
    }


def print_test_results(algorythm_name, results):
    print(f"{algorythm_name}:")
    for amount, time in results.items():
        print(f"{amount}: {time} seconds")


print_test_results("find_min_coins", test_algorythm(find_min_coins))
print_test_results("find_coins_greedy", test_algorythm(find_coins_greedy))
