def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is positive".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer

    """
    if a > 0 or b > 0:
        return True 
    else:
        return False
    return a, b

print(main(-5, 4))