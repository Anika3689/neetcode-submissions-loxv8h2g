class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashed_strings = {}
        for string in strings:
            hashed_rep = ''
            for i in range(len(string)-1):
                #print(string, (ord(string[i+1]) - ord(string[i])))
                char_dist = ((ord(string[i+1]) - ord(string[i])) % 26)
                hashed_rep += str(char_dist) + ','

            if hashed_rep in hashed_strings:
                hashed_strings[hashed_rep].append(string)
            else:
                hashed_strings[hashed_rep] = [string]
        
        #print(hashed_strings)

        res = []
        for hashed_rep in hashed_strings:
            res.append(hashed_strings[hashed_rep])
        return res