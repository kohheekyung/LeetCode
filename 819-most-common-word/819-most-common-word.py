class Solution:
    
    def mostCommonWord_(self, paragraph: str, banned: List[str]) -> str:
        #52 ms
        #14 mb
        
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
    
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
                
        paragraph = re.sub('[^\w]',' ',paragraph ).lower()
        words = paragraph.split()
        words = [word for word in words if word not in banned]
        
        
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]