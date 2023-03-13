def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if a > 9 and a < 100:
        return True
    else:
        return False

    return a

print(main(10))


