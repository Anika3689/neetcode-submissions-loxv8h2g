class Solution:
    def isPerfectSquare(self, num: int, l=1, r=None) -> bool:
        if r is None:
            r = num
        if l > r:
            return False

        mid = (l + r) // 2
        squared = mid ** 2
        if squared == num:
            return True
        elif squared < num:
            return self.isPerfectSquare(num, mid + 1, r)
        else:
            return self.isPerfectSquare(num, l, mid - 1)
