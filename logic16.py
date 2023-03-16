def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if len(str(a)) == 5:
        return True
    else:
        return False

    return a

print(main(1256))






