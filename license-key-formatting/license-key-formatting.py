class Solution(object):
    
    
    # Time complexity - O(N) check every char in N sized string
    # Space complexity - O(1)
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

#         CleanLicenseKey = ''
        
#         # split the first and remaining group
#         firstGroup = s.split('-')[0] + '-'
#         remainGroup = s.split(firstGroup)[1]
        
#         CleanLicenseKey += firstGroup
        
#         # loop the remain group
#         tmpNum = 0
#         for currChar in remainGroup:
#             if tmpNum == k :
#                 CleanLicenseKey += '-'
#                 tmpNum = 0
#             CleanLicenseKey += currChar.upper()
#             tmpNum += 1
        
#         return CleanLicenseKey
    
        # ignore '-'
        # make char all upper case
        # reverse
        s = s.replace('-','').upper()[::-1]
        
        result = ''
        count = 0
        for currChar in s :
            if count == k :
                result += '-'
                count = 0
            result += currChar
            count += 1
        return result[::-1]
    
            
        