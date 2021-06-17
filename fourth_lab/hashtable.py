class Hashtable:
    def __init__(self, size: int, hash_func):
        self.__collection = [[] for _ in range(size)]
        self.hash_func = hash_func
        self.size = size

    def insert(self, key, value):
        hash_key = self.hash_func(key) % self.size
        key_exists = False
        bucket = self.__collection[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = self.hash_func(key) % self.size
        bucket = self.__collection[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def get_collection(self):
        return str(self.__collection)

    def delete(self, key):
        hash_key = hash(key) % self.size
        key_exists = False
        bucket = self.__collection[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))

    def printt(self):
        print(self.__collection)

    def __str__(self):
        return "\n".join(["\n".join([f'{i[0]}:{i[1]}' for i in x]) for x in self.__collection if x != []])

    def __len__(self):
        return sum([sum([1 for i in x]) for x in self.__collection if x != []])
