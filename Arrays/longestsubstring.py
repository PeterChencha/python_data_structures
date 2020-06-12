"""Given a string, find the length of the longest substring without repeating characters."""

def lengthOfLongestSubstring(s):
    letter_set = set()
    lengths = []
    count = 0
    current_pointer = 0

    while current_pointer < len(s):
        if s[current_pointer] not in letter_set:
            count = count + 1
            letter_set.add(s[current_pointer])
        else:
            lengths.append(count)
            count = 1
            letter_set.clear()
            letter_set.add(s[current_pointer])
        current_pointer = current_pointer + 1

    if len(lengths) == 0:
        return len(s)
    else:
        return max(lengths)

def lengthLongest(s):
    letter_dict = {}
    max = 0
    start = 0
    for i, value in enumerate(s):
        if value in letter_dict.keys():
            sums = letter_dict[value] + 1
            if sums > start :
                start = sums

        num = i - start + 1
        if num > max :
            max = num
        letter_dict[value] = i

    return max

test = "abcabcbb"

result = lengthLongest(test)

print(result)
