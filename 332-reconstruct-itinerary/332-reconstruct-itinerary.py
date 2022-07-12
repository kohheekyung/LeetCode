class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        sort 후
        [['ATL','JFK'],['ATL', 'SFO'], ['JFK', 'ATL'], ['JFK', 'SFO'], ['SFO', 'ATL']]
        '''
        
        def dfs(curr_from, curr_tickets):
        
            if len(curr_tickets) == 1:
                result.append(curr_tickets[0][1])
                result.append(curr_tickets[0][0])
                return True

            for ticket in curr_tickets:
            
                # 티켓들 중에 찾고있는 현 from이 있으면
                if ticket[0] == curr_from:    
                    
                    # 다음 from 확인
                    next_from = ticket[1]
        
                    # 다음 티켓 후보
                    next_tickets = curr_tickets[:]
                    next_tickets.remove(ticket)
                    
                    # 다음 시작점의 도착점이 있는지 확인
                    next_exist = dfs(next_from, next_tickets)
                    
                    # 존재하면 경로 삽입
                    if next_exist:
                        result.append(ticket[0])
                        return True
                    # 존재하지 않으면 계속 찾음
                    else:
                        continue
                        
            # 못찾으면 False 반환
            return False
            
        
        # smaller lexical order를 위해 sort하고 시작
        tickets = sorted(tickets, key = lambda x:(x[0], x[1]))
        
        result = []
        
        # JFK로 시작 
        dfs("JFK",tickets)
        
        return result[::-1]
    
    