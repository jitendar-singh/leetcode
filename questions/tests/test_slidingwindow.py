from questions.slidingwindow import Solution
from typing import List
import unittest
class TestClass(unittest.TestCase):

    def test_slidingwindow(self,arr: List[int],wsize: int)->int:
        s = Solution()
        self.assertEquals(s.slidingwindow([1,1,2,3,4,5,6],3),15,f'Expected 15 got {s.slidingwindow([1,1,2,3,4,5,6],3)}')

if __name__ == '__main__':
    unittest.main()
    