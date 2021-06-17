class Solution:
    def repeatingSubstring(self,arr: str)->None:
        #aaaabbccccc
        left = 0
        right = 1
        count = 1
        m = {}
        while(left < len(arr) and right < len(arr)):
            if(arr[left]==arr[right]):
                count+=1
                m[arr[left]] = count # a:4
                left = right # l=3 
                right+=1 #r=4
            else:
                count = 1
                left = right
                right+=1
        allvalues = m.values()
        count = max(allvalues)
        maxkey = max(m,key=m.get)
        print(maxkey)
        print(maxkey*count,"#",count)
s= Solution()
a = "aacceeeeeeeeeeeebbbbc"
s.repeatingSubstring(a)