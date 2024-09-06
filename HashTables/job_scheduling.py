class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))  # Sort jobs by start time
        n = len(jobs)

        @lru_cache(None)
        def rec(i=0):
            if i == len(jobs):
                return 0
            
            starts_at, ends_at, job_profit = jobs[i]
            # Option 1: Take the current job

            next_start_idx = bisect.bisect_left(jobs,(ends_at,-1,-1))
            opt1 = job_profit + rec(i=next_start_idx)

            # Option 2: Skip the current job, find the next suitable job
            opt2 = rec(i+1)
            return max(opt1, opt2)
        return rec()
        # 1 2 3 4 5 6
        # 0 1 2 3 4 5
        # -----
        #   50
        #   -----
        #     10 
        #     -----
        #      40
        #     -------
        #       70
        
        # starts_at=0(i) => 50 (profit[i]) + next_job(starts_at=end_time[i])
        #   or starts_at(startTime[i+1]-1)
        
        # starts_at=2(i)=>


        # if i pick one job from i i cannot start another job until that ends
            # for jobs that start at index i
            
                # option 1: i choose that job
                # job_profit(starts_at=i) = profit[i] + job_profit(starts_at=endTime[i])

                # option 2: i dont chose that job
                # job_profit(starts_at=i) =  job_profit(starts_at=startTime[i+1])
        






                