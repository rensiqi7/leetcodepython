class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i * i:n:i] = [0] * (int(n - i * i - 1) / i + 1)
        return sum(s)

        """
        if n <= 2:
            return 0

        is_prime = [True] * n
        num = n / 2
        for i in xrange(3, n, 2):
            if i * i >= n:
                break

            if not is_prime[i]:
                continue

            for j in xrange(i*i, n, 2*i):
                if not is_prime[j]:
                    continue

                num -= 1
                is_prime[j] = False

        return num
        """
