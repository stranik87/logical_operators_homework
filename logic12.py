def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if a%10 == a//10:
        return True
    else:
       return False
        
    return a



print(main(32))