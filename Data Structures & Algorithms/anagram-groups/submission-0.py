class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #hash map for the list of anagrams

        for s in strs: 
            count = [0] * 26 #takes every letter of the alphabet
            
            for c in s: 
                count[ord(c) - ord('a')] += 1 #maps the character to the correct index on the array, then counts how many
            res[tuple(count)].append(s) #uses tuple as value as cannot take in list in python, appends that count
        return list(res.values())
