class Caesar:
    def encrypt(self, msg: str, k: int) -> str:
        chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        counter = 1
        alphabets = {}
        encrypted_msg = []
        location = 0
        output = ""

        for char in chars:
            alphabets[char] = counter
            counter+=1
        #a 
        for ch in msg:
            if ch == " ":
                encrypted_msg.append("-")
            else:
                location = alphabets[ch]
                desried_char = location+k
                if desried_char > 26:
                    desried_char = desried_char - 26
                for key, value in alphabets.items():
                    if value == desried_char:
                        encrypted_msg.append(key)
        return output.join(encrypted_msg)
            

c = Caesar()
msg = input('Enter your message: ')

encrypted_output = c.encrypt(msg.lower(),4)
print(encrypted_output.replace("-"," "))