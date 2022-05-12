class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            
            # list default dictionary
            anagrams = collections.defaultdict(list)
            
            # define the dictionary key by sorted word
            for word in strs:
                anagrams[''.join(sorted(word))].append(word)    
                
            return list(anagrams.values())