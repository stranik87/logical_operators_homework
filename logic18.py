def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1 = a%10
    x2 = a//10%10
    x3 = a//100%10
    x4 = a//1000%10
    x5 = a//10000%10
    
    if x5<x4<x3<x2<x1:
        return True
    else:
        return False
    return a

print(main(12345))