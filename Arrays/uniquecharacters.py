#Implement an alorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

import time
#IMPLEMENTATION WITH ADDITIONAL DATA STRUCTURE
#IMPLEMENTATION HAS O(N) TIME COMPLEXITY
def uniqueCharacters(string):
    t = time.process_time()
    unique = set()
    for _ in range(len(string)):
        unique.add(string[_])

    if len(string) == len(unique):
        elapsed_time = time.process_time() - t
        print(elapsed_time)
        return True
    else:
        elapsed_time = time.process_time() - t
        print (elapsed_time)
        return False

#IMPLEMENTATION WITHOUT ADDITIONAL DATA STRUCTURE
#IMPLEMENTATION HAS O(N^2) TIME COMPLEXITY OWING TO THE TWO FOR LOOPS
def uniqueCharactersNoBuiltIn(string):
    string = string.lower()
    for i in range(len(string)):
        for j in range(i, len(string) - 1):
            if string[i] == string[j + 1]:
                return False

    return True


test = "Peter"
test1 = "Pot"
test2 = "KAyak"
test3 = "Unique"
#result = uniqueCharacters(test)
result = uniqueCharactersNoBuiltIn(test2)
print (result)
