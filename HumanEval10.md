docstring of the HumanEval10:
```
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
```
primary base solution:
```
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
      
    for i in range(len(string))):
        if string[i:] == string[i:][::-1]:
            return string + string[:i][::-1]
    
    return string
```
0.py : logically incorrect and fails doctests
1.py : logically incorrect however it can be easily correct by changing the condition in Line 23 by removing the not operator.
2.py : logically correct. Passes doctests however space complexity gets bigger with larger string inputs
3.py : logically correct however multiple function calls makes it slower than the base solution
4.py : copy of 2.py
5.py : copy of 3.py except with different variable names
6.py : copy of 3.py
7.py : fails the doctest of an edge case however for a valid inputit returns the right result. It is also worse in terms of space complexity
8.py : logically incorrect
9.py : passes all doctests and is logically correct however worse in terms of time complexity. Makes an unnecessary condition that will never be true
10.py : copy of 2.py



