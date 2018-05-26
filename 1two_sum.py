class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        look_for = {}
        for n, x in enumerate(nums):
            try:
                return look_for[x], n
            except KeyError:
                look_for.setdefault(target - x, n)


'''
Here you build the dictionary of values on an as-needed basis. The dictionary \
is keyed by the values you are seeking, and for each value you track the \
index of its first appearance. As soon as you come to a value that satisfies \
the problem, you're done. There is only one for loop.

The only other detail is to add 1 to each index to satisfy the ridiculous \
requirement that the indices be 1-based. Like that's going to teach you about\
 Python programming.

Keys are added to the dictionary using the setdefault function, since if the \
key is already present you want to keep its value (the lowest index).
'''
