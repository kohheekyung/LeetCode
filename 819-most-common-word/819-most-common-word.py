class Solution:
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        
        # Preprocess string
        # ^ : not
        # \w: word character
        # replace non-word character to ''
        # make all lower case
        paragraph = re.sub('[^\w]',' ',paragraph ).lower()
        # or
        #paragraph = re.sub('[!?'',;.]','',paragraph ).lower()
        
        words = paragraph.split()
  
        counts = collections.defaultdict(int)       
        for word in words:
            if word not in banned:
                counts[word] += 1
        
        return max(counts, key=counts.get)
                
        
            