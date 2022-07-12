class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        
        def dfs(curr_from, curr_tickets):
        
            if len(curr_tickets) == 1:
                result.append(curr_tickets[0][1])
                result.append(curr_tickets[0][0])
                return True

            for ticket in curr_tickets:
                
                if ticket[0] == curr_from:
                    
                    next_from = ticket[1]
        
                    next_tickets = curr_tickets[:]
                    next_tickets.remove(ticket)
                    
                    
                    #result.append(ticket[0])
                    
                    
                    next_exist = dfs(next_from, next_tickets)
                    if next_exist:
                        result.append(ticket[0])
                        return True
                    else:
                        continue
            return False
            
        
     
        tickets = sorted(tickets, key = lambda x:(x[0], x[1]) )
        print(tickets)
        
        result = []
        
        dfs("JFK",tickets)
        
        return result[::-1]