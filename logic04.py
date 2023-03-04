def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    x = ((int(a))%2 == 0), ((int(b))%2 == 0)
    return  x


print(main(2, 1))