class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Key is a sorted word and the value is a list of all its anagrams
        anagramGroups = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagramGroups:
                anagramGroups[sorted_string].append(string)
            else:
                anagramGroups[sorted_string] = [string]
        
        return [anagramGroups[anagram] for anagram in anagramGroups]