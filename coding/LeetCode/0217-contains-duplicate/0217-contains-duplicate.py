class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            curr_set_size = len(nums_set)
            nums_set.add(num)
            if curr_set_size == len(nums_set):
                return True
        return False