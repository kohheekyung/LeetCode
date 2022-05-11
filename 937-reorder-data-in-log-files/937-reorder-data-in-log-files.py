class Solution:
    
    def sortfunc(x):
        return x.split()[1:] , x.split()[0]
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter_logs = []
        digit_logs = []
        
        # split letter logs and digit logs
        for log in logs:
            
            split_log = log.split()
            
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        # sort letter logs by content.
        # if contents is same, sort by identifier
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letter_logs + digit_logs