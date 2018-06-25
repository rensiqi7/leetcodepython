
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        index = 0
        hashTable = {}
        output = []
        for str in strs:
            hash = ''.join(sorted(str))
            if (hash in hashTable):
                output[hashTable[hash]].append(str)
            else:
                hashTable[hash] = index
                output.append([str])
                index += 1
        return output
