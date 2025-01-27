def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]
example=input()
word = "madam"
phrase = "A man a plan a canal Panama"
print(is_palindrome(word))  # Output: True
print(is_palindrome(phrase))  # Output: True
print(is_palindrome(example))