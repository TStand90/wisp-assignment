from functools import cache


@cache
def special_math(number: int) -> int:
    """
    This function uses the "@cache" decorator to save some time doing the recursion. It will still return a
    RecursionError if the number is too large, but I wanted to include this because I was very proud of myself for
    remembering that @cache exists.
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return number + special_math(number - 1) + special_math(number - 2)


def find_closest_number_in_cache(current_number: int, special_math_cache: dict[int, int]) -> int:
    """
    Given a number, find the closest match in a given cache by iterating down until a number is found in the cache.
    In case a number is not found, return 0.
    """
    while current_number >= 0:
        if current_number in special_math_cache:
            return special_math_cache[current_number]

        current_number -= 1

    # Theoretically, this should never be reached.
    return 0


def special_math_without_recursion(number: int) -> int:
    """
    This is the same function as above, but implemented without recursion. It can handle much larger numbers since
    it won't be running into Python's maximum recursion limit.
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1

    # This is the "cache" that will memoize the calculated numbers.
    special_math_cache = {
        0: 0,
        1: 1
    }

    iterator = 2

    while iterator <= number:
        # Find the values for the iterator -1 and -2 in the cache.
        number_1 = find_closest_number_in_cache(current_number=iterator - 1, special_math_cache=special_math_cache)
        number_2 = find_closest_number_in_cache(current_number=iterator - 2, special_math_cache=special_math_cache)

        # Add this number's value to the cache.
        special_math_cache[iterator] = iterator + number_1 + number_2

        iterator += 1

    return special_math_cache[number]
