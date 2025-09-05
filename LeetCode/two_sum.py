class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for indice, value in enumerate(nums):
            addon = self.addition(value, target)

            try:
                complement = hash_table[str(addon)]

                return [complement, indice]
            except Exception as e:
                hash_table[str(value)] = indice
                pass

    def addition(self, num: int, target: int):
        return target - num

