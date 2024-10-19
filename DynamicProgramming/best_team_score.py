class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(scores,ages))
        players.sort()
        dp = [ score for score, _ in players]

        for i in range(len(players)):
            currScore, currAge = players[i]
            for j in range(i):
                _, previousAge = players[j]
                if currAge >= previousAge:
                    # current total score or include all previous score that would
                    # have been possible from index j
                    dp[i] = max(dp[i], currScore + dp[j])
        
        return max(dp)

        
        
        # team_score = sum(players)
        # in_conflict(i,j) ages[i] < ages[j] and scores[i] > scores[j]


        players = list(zip(ages,scores))
        players.sort() # sort by age


        # 1 2 3 4  5
        # 1 3 4 10 15
        # prev_score < next_score condition should hold if it doesnt
            # skip that player and keep prev_score intact
            # skip prev_score and keep your player_score instead
        
        # highest overall score of all teams
        highest_score = 0
        if len(scores) == 1: return scores[0]
        mem = {}
        def rec(i=1,prev_best_score=players[0][1]):
            max_score = prev_best_score
            
            if i == len(scores): return prev_best_score
            if (i,prev_best_score) in mem: return mem[(i,prev_best_score)]
            next_score = players[i]
            

            # conflict
            if prev_best_score > next_score:
                # disregard curr player
                opt1 = rec(i+1,next_score)
                # disregard incoming player
                opt2 = rec(i+1,prev_best_score)
                max_score = max(max_score,opt1,opt2)
            else:
                # keep both
                opt3 = rec(i+1,prev_best_score+next_score)
                max_score = max(max_score, opt3)
            
            mem[(i,prev_best_score)] = max_score
            return max_score
        return rec()
            
