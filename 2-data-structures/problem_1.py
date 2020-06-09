from collections import deque


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = deque(maxlen=capacity)
        self.data = {}
        # Initialize class variables
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.data:
            self.cache.remove(self.cache[self.cache.index(self.data[key])])
            self.cache.append(self.data[key])
            return self.data[key][1]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        cache_object = (key, value)
        if len(self.cache) >= self.capacity:
            remove = self.cache.popleft()
            del self.data[remove[0]]
        self.cache.append(cache_object)
        self.data[key] = cache_object

    def size(self):
        return len(self.cache)


# Test 1
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Test 2
lru_cache = LRU_Cache(1000)

lru_cache.set(1, 1)
lru_cache.set(2, 2)
lru_cache.set(3, 3)

print(lru_cache.get(2))  # expected 2

# Test 3
lru_cache = LRU_Cache(10)

lru_cache.set(1, 1)
lru_cache.set(2, 2)
lru_cache.set(3, 3)

print(lru_cache.get(4))  # expected -1
print(lru_cache.size())  # expected 3
