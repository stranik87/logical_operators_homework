def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b = str(a)

    if b[0] == b[1]:
        return True
    else:
        return False
        
    return a



print(main(34))