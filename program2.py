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
        
        total_sum = 0  # Default value is 0 as empty string may also come.
        length = len(s)
        
        for i in range(length):
            num_value = roman_data[s[i]]
            # Check if this is not the last character and the current value is less than the next one
            if i + 1 < length and num_value < roman_data[s[i + 1]]:
                total_sum -= num_value  # Subtract if less than the next
            else:
                total_sum += num_value  # Otherwise, add
        
        return total_sum
