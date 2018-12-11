class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        m = len(beginWord)
        left = {beginWord}
        right = {endWord}
        ct = 2
        while left and right:
            if len(left) > len(right):
                left, right = right, left
            to = set()
            for x in left:
                for i in range(m):
                    for c in 'zxcvbnmasdfghjklqwertyuiop':
                        tp = x[:i] + c + x[i + 1:]
                        if tp in right:
                            return ct
                        if tp in wordList:
                            wordList.remove(tp)
                            to.add(tp)
            left = to
            ct += 1
        return 0
