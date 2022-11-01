class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        output = 0
        odd_found = False

        for count in c.values():
            output += int(count/2) * 2
            if output % 2 == 0 and count % 2 == 1:
                output += 1
        return output                    
