class Solution:
    def removeDuplicate(self,str1: str)->str:
       # Store the string without
        # duplicate elements
        st = []
        
        # Store the index of str
        i = 0
        
        # Traverse the string str
        while i < len(str1):
         
            # Checks if stack is empty or top of the
            # stack is not equal to current character
            if len(st)== 0 or str1[i] != st[-1]:
                st.append(str1[i])
                i += 1
                
            # If top element of the stack is
            # equal to the current character
            else:
                st.pop()
                i += 1
                
        # If stack is empty
        if len(st)== 0:
            return("")
            
        # If stack is not Empty
        else:
            short_string = ""
            for i in st:
                short_string += str(i)
            return(short_string)
                    

ss = Solution()
str2 = ss.removeDuplicate("jitendarrssinghhgg")
print(str2)

