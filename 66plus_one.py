class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # str_ = "".join(str(d) for d in digits)
        # str_ = int(str_) + 1
        # str_ = str(str_)
        # return [int(s) for s in str_]

        rem = 1
        count = len(digits) - 1
        add_cell = False
        while count >= 0:
            if count == 0:
                if (digits[count] + rem) > 9:
                    add_cell = True
            val = digits[count]
            digits[count] = (val + rem) % 10
            rem = (val + rem) // 10
            count -= 1

        if add_cell:
            return [rem] + digits[:]

        return digits


"""
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
                break
            else:
                digits[i] -= 10
        if carry == 1:
            digits.insert(0, 1)
        return digits
"""
