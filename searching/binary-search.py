class Binary:
    def binary_search(self,data: list[int],target: int)-> bool:
        low = 0
        high = len(data)-1
        mid = 0
        data.sort()
        while low <= high:
            mid = (low+high) // 2
            if target == data[mid]:
                return True
            elif target > data[mid]:
                low = mid + 1
            else:
                high = mid -1
        return False

b = Binary()
data = [2,4,5,7,8,9,12,89,90,78,99,43,33,18,17,19,73,91,92,5,881]
target = 17
result = b.binary_search(data,target)
print(result)
