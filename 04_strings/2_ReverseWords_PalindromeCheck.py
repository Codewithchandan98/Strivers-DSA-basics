# Brute force :

# def reverseWords(s: str) -> str:
#     words = s.split()
#     reversed_words = words[::-1]
#     return ' '.join(reversed_words)

# def isPalindrome(s: str) -> bool:
#     clean = ''.join(c.lower() for c in s if c.isalnum())
#     return clean == clean[::-1]

# Optimal code :

def isPalindrome(s: str) -> bool:
    left, right = 0, len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True

user_input = input("Enter a string to check if its a palindrome:")
result = isPalindrome(user_input)
if result:
    print("the string is a palinfrome")
else:
    print("the string is not a palindrome.")    
                                              
