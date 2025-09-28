class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vocabulary = {}

        longest_substring = 0
        big_substring = 0
        subsequence = 0
        index = 0

        while (index < len(s)):
            char = s[index]

            if char in vocabulary:
                position_iteration = vocabulary[char]
                position = position_iteration[0]
                iteration = position_iteration[1]

                if iteration == subsequence:
                    if big_substring > longest_substring:
                        longest_substring = big_substring
                    big_substring = 0
                    subsequence += 1
                    index = position 
                else:
                    vocabulary[char] = (index, subsequence)
                    big_substring += 1
            else:
                vocabulary[char] = (index, subsequence)
                big_substring += 1
            index += 1

        if big_substring > longest_substring:
            return big_substring
        
        return longest_substring 


teste = Solution()
print(teste.lengthOfLongestSubstring("pwwkew"))

