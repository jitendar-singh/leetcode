import string
class Solution:
    def __init__(self, store: dict):
        alphabets = list(string.ascii_lowercase)
        self.store = store
        for chs in alphabets:
            self.store[chs] = 0

    def unique(self, s: str) -> bool:
        for ch in s:
            self.store[ch] = self.store[ch]+1
        # print(self.store)
        for ch in self.store.keys():
            if self.store[ch] > 1:
                return False
        return True

st = {}
ss = Solution(st)
s = 'abcdee'
is_unique = ss.unique(s)
print(is_unique)