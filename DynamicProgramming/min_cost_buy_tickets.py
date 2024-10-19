class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        mem = {}
        def dfs(i=0):
            if i == len(days): return 0
            if i in mem: return mem[i]
            if i > days[-1]: return 0 # already can travel to the end
            min_option = float('inf')
            for days_to_add, cost in zip([1,7,30],costs):
                # find next day where you need to buy
                j = i
                valid_till = days[i] + days_to_add
                while j < len(days) and days[j] < valid_till:
                    j += 1
                opt = cost + dfs(j)
                min_option = min(min_option,opt)
            mem[i] = min_option
            return min_option
        return dfs()

        # min(dollars_spent given you travel every day)
            # options: 1,7,30 day pass
        
        # days=[1,4,6,7,8,20] costs=[2,7,15], days_added = [1,7,30]
            # days needs to be sorted
            # only iterate on the days you need to travel
            
            # 1,  valid_till=1  , c= +2
            # 4.. valid_till= 4+7=11, c=+2+7
            # 6..
            # 7..
            # 8.. 
            # 20 valid_till=20+1 , c=+2+7+2=11

        # at a given day i
            # if i have a valid ticket purchased , valid_till >= i youre good
            # or spend on a ticket, that will give you
                        # cost[t] + valid_till + 
        cache = {}
        def rec(i=0,valid_till=0):
            if i == len(days): return 0 # no more cost needed
            key = (i,valid_till)
            if key in cache: return cache[key]
            # spend for 3 types of tickets
            
            # already have a valid ticket
            opt0 = 0
            if valid_till < days[i]:
                opt0 = float('inf')
            
            # need to buy a ticket
            opt1 = costs[0] + rec(i+1,max( valid_till, days[i]+1 ))
            opt2 = costs[1] + rec(i+1,max( valid_till, days[i]+7) )
            opt3 = costs[2] + rec(i+1,max( valid_till, days[i]+30) )
            ans = min(opt0,opt1,opt2,opt3)
            cache[key] = ans
            return ans
        return rec()

        # rec(3,9)


        

