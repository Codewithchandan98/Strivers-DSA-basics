
def largestOddNumber(num: str) -> str:
    for i in reversed(range(len(num))):
        if int(num[i]) %2 == 1:
            return num[:i + 1]
    return ""    
num = "420538"
result = largestOddNumber(num)
print("Largest odd number substring:", result)