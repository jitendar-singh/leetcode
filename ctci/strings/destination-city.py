class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        outgoing_count = {}
        for path in paths:
            city_a, city_b = path
            print(city_a,'->',city_b)
            outgoing_count[city_a] = outgoing_count.get(city_a,0)+1
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)
            print(outgoing_count)

        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city

s= Solution()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
output = s.destCity(paths)
print(output)