def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if a > 99 and a < 1000:
        return True
    else:
        return False
    return a

print(main(123))