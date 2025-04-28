def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
    
    return str(s).islower()
a=str(input())
print(main(a))