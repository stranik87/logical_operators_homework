def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    
    x = a%10 
    x1= a//10
    if (x+x1)%2 ==0:
        return True
    else:
        return False

    return a





