#Write function, given two strings, decide if one is a permutation of the other

def isPermutation(string1, string2):
    a = sorted(string1)
    b = sorted(string2)

    if len(string1) == len(string2):
        for _ in range(len(string1)):
            if a[_] == b[_]:
                return True
            else:
                return False
    else:
        return False

test = "ABCD"
test1 = "CAB"
result = isPermutation(test,test1)
print(result)
