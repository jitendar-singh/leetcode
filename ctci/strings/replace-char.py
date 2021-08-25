class Solution:
    def replace_char(self, s: str) -> str:
        # actual_len = 0
        lenght = len(s)
        key = f'%20'
        nstr = []
        while(lenght>=0):
            while(s[lenght-1]==' '):
                lenght-=1
            if s[lenght] == ' ':
                nstr.insert()
                lenght-=1
            else:
                nstr.append(s[lenght])
                lenght-=1
        print(nstr)
        # return nstr

ss = Solution()
s = 'Mr Jitendar Singh       '
nstr = ss.replace_char(s)
print(nstr)
