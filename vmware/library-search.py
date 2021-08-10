
class Solution:
    def search(self,books: list[str],keyword: str):
        output = []
        for book in books:
            if book.startswith(keyword):
                output.append(book)
        if len(output)>0:
            return output
        else:
            print(" No match found")
            return -1

s = Solution()
books = ["hello","happylife","Algorithm","DSA","Python","happynewyear"]
key = "Ds"
out = s.search(books,key)
print(out)




