"""
Implement Chloe's solution to the 12 coins problem
2022-03-26

"""

def weigh(left, right):
    """
    Weigh two groups of coins using the balance scale
    Args:
        left: list of positive numbers representing coin weights (can also be an int or float for a single number)
        right: list of positive numbers representing coin weights (can also be an int or float for a single number)
    Returns:
        integer:
            1 if left is heavier
            -1 if left is lighter (right is heavier)
            0 if equal
    """

    left_weight = left if isinstance(left, (int, float)) else sum(left)
    right_weight = right if isinstance(right, (int, float)) else sum(right)

    if left_weight > right_weight:
        return 1
    elif left_weight < right_weight:
        return -1
    else:
        return 0

    return None


def solve_4_heavy_4_light_2_ws(heavy_coins, light_coins, real_coins, verbose=False):
    """
    Given two lists of 4 coin weights, where the first list is heavier, identify the fake coin in at most 2 weighings
    Args:
        heavy_coins: list of 4 numbers representing coin weights
        light_coins: list of 4 numbers representing coin weights, such that sum(light_coins) < sum(heavy_coins)
        real_coins: list of 4 numbers representing coin weights, where all 4 coins are known to be real
    Returns:
        dictionary with keys:
            index: number between 0 and 3 representing index of fake coin within its own list (heavy_coins or light_coins)
            weight: 1 if the fake coin is heavy, -1 if the fake coin is light
    """
    
    w1 = weigh(heavy_coins[0:1] + light_coins[0:3], light_coins[3:4] + real_coins[0:3])
    
    if w1 == 1:
        w2 = weigh(heavy_coins[0], heavy_coins[1])
        if w2 == 1:
            solution = {"weight": 1, "index": 0}
        elif w2 == 0:
            solution = {"weight": -1, "index": 3}
        else:
            raise Exception("this should never happen")
            pass
    elif w1 == -1:
        solution = {"weight": -1}
        w2 = weigh(light_coins[0], light_coins[1])
        if w2 == 1:
            solution["index"] = 1
        elif w2 == -1:
            solution["index"] = 0
        else: # w2 == 0:
            solution["index"] = 2
    else: # w1 == 0
        solution = {"weight": 1}
        w2 = weigh(heavy_coins[1], heavy_coins[2])
        if w2 == 1:
            solution["index"] = 1
        elif w2 == -1:
            solution["index"] = 2
        else:
            solution["index"] = 3

    if verbose:
        print(
            "Coin number {index} out of 4 was fake and {weight}".format(
                index = solution["index"] + 1, 
                weight = "heavy" if solution["weight"] == 1 else "light"
            )
        )
    
    return solution


def solve_4_fake_4_real_2_ws(coins, real_coins, verbose=False):
    """
    TODO: indexing on w2 after fixing weigh function to accept single numbers
    Given a list of 4 coin weights where one coin is fake and a reference list of 4 coin weights where all coins are real, identify the fake coin in at most 2 weighings
    Args:
        coins: list of 4 numbers representing coin weights where one coin is fake
        real_coins: list of 4 numbers representing coin weights were all coins are real
    Returns:
        dictionary with keys:
            index: number between 0 and 3 representing index of fake coin in coins list
            weight: 1 if the fake coin is heavy, -1 if the fake coin is light
    """

    w1 = weigh(coins[0:3], real_coins[0:3])

    
    if abs(w1) == 1:
        w2 = weigh(coins[0], coins[1])
        solution = {"weight": w1}
        if w2 == 0:
            solution["index"] = 2
        else:
            solution["index"] = 0 if w1 == w2 else 1
    else: # w1 == 0
        w2 = weigh(coins[3], real_coins[0])
        solution = {
            "index": 3,
            "weight": w2
        }

    if verbose:
        print(
            "Coin number {index} out of 4 was fake and {weight}".format(
                index = solution["index"] + 1, 
                weight = "heavy" if solution["weight"] == 1 else "light"
            )
        )
    
    return solution


def solve_12_coins_3_ws(coins, verbose=True):
    """
    Naive/brute force algorithm, will clean up code later
    Given a list of 12 coin weights, identify the fake coin in at most 3 weighings
    Args:
        coins: list of 12 numbers representing coin weights
        verbose: boolean, True to print messages, False to not
    Returns:
        dictionary with keys:
            index: number between 0 and 11 representing index of fake coin in coins list
            weight: 1 if the fake coin is heavy, -1 if the fake coin is light
    """

    group_a = coins[0:4]
    group_b = coins[4:8]
    group_c = coins[8:12]

    w1 = weigh(group_a, group_b)

    
    if w1 == 1:
        temp = solve_4_heavy_4_light_2_ws(heavy_coins=group_a, light_coins=group_b, real_coins=group_c)
        solution = {
            "index": temp["index"] + (0 if temp["weight"] == 1 else 4),
            "weight": temp["weight"]
        }
    elif w1 == -1:
        temp = solve_4_heavy_4_light_2_ws(heavy_coins=group_b, light_coins=group_a, real_coins=group_c)
        solution = {
            "index": temp["index"] + (4 if temp["weight"] == 1 else 0),
            "weight": temp["weight"]
        }
    else: # w1 == 0
        temp = solve_4_fake_4_real_2_ws(coins=group_c, real_coins=group_a)
        solution = {
            "index": temp["index"] + 8,
            "weight": temp["weight"]
        }

    if verbose:
        print(
            "Coin number {index} out of 12 was fake and {weight}".format(
                index = solution["index"] + 1, 
                weight = "heavy" if solution["weight"] == 1 else "light"
            )
        )

    return solution


if __name__ == "__main__":
    for i in range(12):
        for j in [1, -1]:
            coins = [2] * 12
            coins[i] = coins[i] + j
            print(coins)
            solve_12_coins_3_ws(coins, verbose=True)