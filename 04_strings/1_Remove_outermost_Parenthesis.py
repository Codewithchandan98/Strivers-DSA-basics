
# Brute Force Approach :

# Time: O(N), Space: O(N)
# where N is the length of input string

# def removeOuterParentheses(s: str) -> str:
#     result = []
#     balance = 0
#     start = 0
#     
#     for i, char in enumerate(s):
#         if char == '(':
#             balance += 1
#         else:
#             balance -= 1
#         
#         # If primitive ends
#         if balance == 0:
#             # Remove outermost (start and end)
#             result.append(s[start + 1:i])
#             start = i + 1
#     
#     return ''.join(result)

#optimal solution :

def removeOuterParentheses(s: str) -> str:
       result = []
       balance = 0

       for char in s:
              if char == '(':
                if balance > 0:
                          result.append(char)
                balance += 1 
              else:
                   balance -= 1
                   if balance > 0:
                       result.append(char)

       return ''.join(result)                           

input_str = "(()())(())"
print("Input:", input_str)
print("Output:", removeOuterParentheses(input_str))
