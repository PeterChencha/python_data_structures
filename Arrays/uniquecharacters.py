#Implement an alorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

import time
#BOTH FUNCTION HAVE O(n) TIME COMPLEXITY
#THOUGH SECOND FUNCTION HAS O(1) SPACE COMPLEXITY

#IMPLEMENTATION WITH ADDITIONAL DATA STRUCTURE
def uniqueCharacters(string):
    t = time.process_time()
    unique = set()
    for _ in range(len(string)):
        unique.add(string[_])

    if len(string) == len(unique):
        elapsed_time = time.process_time() - t
        print (elapsed_time)
        return True
    else:
        elapsed_time = time.process_time() - t
        print (elapsed_time)
        return False

#IMPLEMENTATION WITHOUT ADDITIONAL DATA STRUCTURE
def uniqueCharactersNoExtraDataStructure(string):
    t = time.process_time()
    for _ in string:
        if string.count(_) > 1:
            elapsed_time = time.process_time() - t
            print (elapsed_time)
            return False
        else:
            elapsed_time = time.process_time() - t
            print (elapsed_time)
            return True



test = "Peter"
test1 = "Pot"
#result = uniqueCharacters(test)
result = uniqueCharactersNoExtraDataStructure(test)
print (result)
