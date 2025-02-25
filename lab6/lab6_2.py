def count_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

input_string = input()
upper, lower = count_letters(input_string)
print(upper)
print(lower)