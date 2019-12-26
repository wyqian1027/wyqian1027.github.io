# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        r = rand7()
        c = rand7()
        n = (r - 1)*7 + c
        if n <= 40:
            return 1 + (n - 1) % 10
        else:
            return self.rand10()