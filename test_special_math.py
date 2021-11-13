from special_math import special_math, special_math_without_recursion


def test_special_math():
    """
    Tests the function "special_math" against known values.

    If the function is implemented properly, this test should be very fast. If it's not, I'm probably not getting the
    job.
    """
    assert special_math(7) == 79
    assert special_math(17) == 10926
    assert special_math(90) == 19740274219868223074


def test_special_math_without_recursion():
    """
    Tests the function "special_math_without_recursion", which should return the same values as "special_math", but it
    should also be able to handle larger numbers without triggering a RecursionError.

    Despite the large number, this test should still be pretty fast.
    """
    assert special_math_without_recursion(7) == 79
    assert special_math_without_recursion(17) == 10926
    assert special_math_without_recursion(90) == 19740274219868223074

    # I'm not going to post the result here since it's ridiculously long, but a RecursionError shouldn't happen here.
    special_math_without_recursion(1000)
