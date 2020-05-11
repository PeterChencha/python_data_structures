class HashTable(object):
    """docstring for HashTable."""
    def __init__(self):
        super(HashTable, self).__init__()
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, value):
        index = self.hashFunction(key)
        print("index to check", index)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hashFunction(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1)%self.size
        return None

    def hashFunction(self, key):
        sum = 0
        if type(key) == str:
            for pos in range(len(key)):
                sum = sum + ord(key[pos])
        else:
            sum = sum + key

        print("Index of hash function", (sum%self.size))
        return sum%self.size

hash = HashTable()
hash.put("name", "Peter Chencha")
hash.put("age", 20)
hash.put(20, 10)

print(hash.get(20))
