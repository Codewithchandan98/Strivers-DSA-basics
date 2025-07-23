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
