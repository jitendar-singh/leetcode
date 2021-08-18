class Solution:
    def __init__(self,d1: dict, d2: dict) -> None:
        self.d1 = d1
        self.d2 = d2
    def permutation(self, s1: str, s2: str) -> bool:
        if len(s1)!= len(s2):
            return False
        else:
            for ch in s1:
                if ch not in self.d1.keys():
                    self.d1[ch] = 1
                else:
                    self.d1[ch] = self.d1[ch]+1
            print(self.d1)

            for ch in s2:
                if ch not in self.d2.keys():
                    self.d2[ch] = 1
                else:
                    self.d2[ch]+=1
            print(self.d2)

            result = self.compare_dict(self.d1,self.d2)
            return result

    def compare_dict(self, d1: dict, d2: dict) -> bool:
        for key in d1.keys():
            if d1[key] != d2[key]:
                return False
        return True
    
d1, d2 = {}, {}
ss = Solution(d1, d2)
s1 = 'abcdd'
s2 = 'cdbza'
result = ss.permutation(s1,s2)
print(result)