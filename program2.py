class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_data = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total_sum = 0 #by default value is 0 as empty string may also come.
        length = len(s)
        
        for i in range(n):
            value = roman_data[s[i]]
            if i + 1 < n and value < roman_data[s[i + 1]]:
                total_sum -= value
            else:
                total_sum += value
        
        return total_sum
