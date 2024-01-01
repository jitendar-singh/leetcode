class Mountain:
    def isValid(self, mount):
        i = 1
        while i < len(mount) and mount[i] > mount[i-1]:
            i+=1
        
        if i == 1 or i == len(mount):
            return False
        
        while i < len(mount) and mount[i] < mount[i - 1]:
            i+=1
        
        return i == len(mount)

mountain = Mountain()
mount = [1,2,3,2,1, 4]

print(mountain.isValid(mount))