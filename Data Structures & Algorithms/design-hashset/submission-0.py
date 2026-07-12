class MyHashSet:

    def __init__(self):
        self.h_set = []

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.h_set.append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        i = self.h_set.index(key)
        self.h_set.pop(i)

    def contains(self, key: int) -> bool:
        return key in self.h_set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)