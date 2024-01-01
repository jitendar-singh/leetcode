class Container:
    def area(self, lst):
        max_area = 0
        l = 0
        r = len(lst) - 1

        while l < r:
            height = min(lst[l],lst[r])
            width = (r - l)
            max_area = max(max_area, (height * width))

            if lst[l] < lst[r]:
                l+=1
            else:
                r-=1
        return max_area

container = Container()
lst = [1,8,6,2,5,7]
max_capacity = container.area(lst)
print(max_capacity)


