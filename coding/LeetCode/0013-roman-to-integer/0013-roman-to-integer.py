roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        total_sum = 0
        curr = 0
        prev = 0
        for letter in reversed(s):
            curr = roman_numerals[letter]
            if curr < prev:
                total_sum -= curr
            else:
                total_sum += curr
            prev = curr
        return total_sum