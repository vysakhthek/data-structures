


"""Function to return weather a  number is panlindrome or not"""
# def is_palindrome(s:str) -> bool:
#     s = s.lower().replace(" ", "")
#     return s==s[::-1]

def is_palindrome(s:str) -> bool:
    s = s.lower().replace(" ", "")
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Python"))


"""Function to return factorial of a number"""
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(6))