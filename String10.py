def main(s):
    """
    A string containing the letter "x" is given. Find the index of the letter "x" in this variable.
    Args:
        s: str
    Returns:
        str: answer
    """
    if 'x' in s:
      return s.index('x')
    return 'x is not found in s'
a=str(input())
print(main(a))