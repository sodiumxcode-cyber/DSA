#Check if the string is palindrome or not
#Leetcode-125

def is_palindrome(s, left, right):
    if left >= right:   # base case
        return True
    
    if s[left] != s[right]:
        return False
    
    return is_palindrome(s, left + 1, right - 1)


s = "madam"
print(is_palindrome(s, 0, len(s) - 1))