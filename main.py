from typing import List


class Solution(object):
    def generate(self, numRows: int) -> List[List[int]]:
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1] for _ in range(numRows)]
        if numRows < 2:return res
        res[1].append(1)

        for i in range(2, numRows):
            for j in range(i-1):
                res[i].append(res[i-1][j]+res[i-1][j+1])
            res[i].append(1)

        return res


if __name__ == '__main__':
    n = int(input())
    res=Solution().generate(n)
    print(res)