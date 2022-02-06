



class Solution(object):
    
    '''
    Approach 1 : Linear Iteration
    
    Plain in text
        1. For each email in the emails array 
            - Iterate over the characters in the email and append each character to the               local name if it is not '.'
            - If the character is '+', do not append the character and break out the                 loop.
        2. Find the domain name using reverse traversal in the given email. and append             int to the string formed till now
            - After cleaning the email insert it into the hash set.
        3. Return the size of the hash set.    
    
    Complexity Analysis
        1. Time Complexity: O(N*M) 
            - In the worst case, we iterate over all the characters of each of the                  emails given.
            - If we have N emails and each email has M characters in it. 
            (Number of emails) * (Number of characters in average email) = N * M
        2. Space Complexity: O(N*M) 
            - If the worst case, when all emails are unique, we will store every email              address given to us in the hash set
    '''
    def numUniqueEmails_A1(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """    
        # Hash set to store all the unique emails.
        uniqueEmails = set()
        
        for email in emails:
            cleanMail = []
            
            # Iterate over each character in email.AssertionError
            for currChar in email:
                # Stop adding characters to localName
                if currChar == '+' or currChar == '@':
                    break

                # Add this character if not '.'.
                if currChar != '.':
                    cleanMail.append(currChar)

            # Compute domain name (substring from end to '@').
            domainName = []
            for currChar in reversed(email):
                domainName.append(currChar)
                if currChar == '@':
                    break
        
            # Reverse domain name and append to locaal name.
            domainName = ''.join(domainName[::-1])
            cleanMail = ''.join(cleanMail)
            uniqueEmails.add(cleanMail + domainName)

        return len(uniqueEmails)
    
    '''
    Approach 2 : Using String Split Method
    
    Algorithm
        1. For each email in the emails array 
            - Split the string into ttwo parts seperated by '@', local name and domain name.       - Split the local name into parts separated by '+'. Since we do not need the part after '+', let the first part be the local name.
            - Remove all '.' from the local name and append the domain name to it.
            - After clearning the email, insert it into the hash set
        2. Return the size of the hash set.    
    
    Complexity Analysis
        1. Time Complexity: O(N*M) 
            - Split method must iterate over all of the characters in each email and the replace method must iterate over all of the characters in each local name. As such, they both require linear time and O(M) operations. Since there are N emails and the average email has M characters in it, the complexity is of order. 
            (Number of emails) * (Number of characters in average email) = N * M
        2. Space Complexity: O(N*M) 
            - In the worst case, when all emails are uniquer, we will store every email address given to us in the has set
    '''
 
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """    
        # Hash set to store all the unique emails.
        uniqueEmails = set()
        
        for email in emails:
            # Split into two parts: local and domain.
            name, domain = email.split('@')
            
            # Split local by '+' and replace all '.' with ''.
            local = name.split('+')[0].replace('.','')
            
            # Concatenate local, '@', and domain.
            uniqueEmails.add(local + '@' + domain)
            
        return len(uniqueEmails)