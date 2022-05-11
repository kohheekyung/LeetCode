class Solution:
    
    def mostCommonWord_(self, paragraph: str, banned: List[str]) -> str:
      
        # Preprocess string
        # ^ : not
        # \w: word character
        # replace non-word character to ''
        # make all lower case
        paragraph = re.sub('[^\w]',' ',paragraph ).lower()
        # or
        #paragraph = re.sub('[!?'',;.]','',paragraph ).lower()
        
        words = paragraph.split()
        words = [word for word in words if word not in banned]
        
        # count word with defalut dict 0
        counts = collections.defaultdict(int)       
        for word in words:
            counts[word] += 1
      
        return max(counts, key=counts.get)
    
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
                
        paragraph = re.sub('[^\w]',' ',paragraph ).lower()
        words = paragraph.split()
        words = [word for word in words if word not in banned]
        
        # use counter func
        counts = collections.Counter(words)
        
        # get firtst most common value list
        most_common = counts.most_common(1)
        
        return most_common[0][0]