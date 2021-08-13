'''
Given an array of sorted integers. We need to find the closest value to the
given number

Array may contain duplicate values and negative numbers

Examples:

Input : arr[] = {1,2,3,4,5,6,7,8}

        target = 11
        output = 9

        9 is closest to 11 in given array
'''
class Solution:
    def search(data: list[int],target: int)-> int:
        lom = 0
        rom = len(data) - 1
        mid = len(data)//2
        
        while(low <= high):
            if data[mid] < target:
                low = mid+1
            else:
                high = mid -1
            