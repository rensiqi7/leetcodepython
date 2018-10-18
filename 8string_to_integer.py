class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.lstrip()

        if not str:
            return 0

        sign = 1
        answer = 0
        if str[0] == '-':
            sign = -1
        if str[0] in ['-', '+']:
            str = str[1:]
        for i in range(len(str)):
            if str[i].isdigit():
                answer = answer * 10 + int(str[i])
            else:
                break

        answer = max(-2**31, min(sign * answer, 2**31 - 1))
        return answer
