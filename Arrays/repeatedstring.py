"""
Lilah has a string,

, of lowercase English letters that she repeated infinitely many times.

Given an integer,
, find and print the number of letter a's in the first

letters of Lilah's infinite string.

For example, if the string
and , the substring we consider is , the first characters of her infinite string. There are occurrences of a in the substring.
"""
def repeated_string(s,n):
    length_of_s = len(s)
    if same_characters(s):
        return n
    multiplier = n//length_of_s
    new_string = s * multiplier
    if len(new_string) < n :
        new_string = new_string + s
    start = 0
    end = n - 1
    ref = 'a'
    count = 0

    while start < end:
        if new_string[start] == ref:
            count = count + 1
            start = start + 1
        elif new_string[end] == ref:
            count = count + 1
            end = end - 1
        else:
            start = start + 1
            end = end - 1

    return count


def same_characters(s):
    start = 0
    end = len(s) - 1
    ref = s[0]

    while start < end + 1:
        if s[start] == ref and s[end] == ref:
            start = start + 1
            end = end - 1
        else:
            return False

    return True


test = "a"
n = 1000000000000
result = repeated_string(test, n)
print(result)
