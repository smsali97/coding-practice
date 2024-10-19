# “USER_FOLLOW” events are never collapsed.
# * “TRENDING_TOPIC” events are collapsed if there are 2 or more consecutive events
# * “DIRECT_MESSAGE” events are collapsed if there are 5 or more consecutive events


# displayText : category (+collapsed)
# `Garage sale`			:`USER_FOLLOW`
# `War in Antarctica`		:`USER_FOLLOW`
# `Weather for tomorrow`	:`TRENDING_TOPIC` (+ 6 more)
# `Party!`			:`DIRECT_MESSAGE` (+ 5 more)
# `Antarctica declared independence`:`TRENDING_TOPIC`


# `Garage sale`			:`USER_FOLLOW`
# `War in Antarctica`		:`USER_FOLLOW`
# `Weather for tomorrow`	:`TRENDING_TOPIC` (+ 6 more)
#      `Expect tornados`		:`TRENDING_TOPIC`
#      `Wind of change?`		:`TRENDING_TOPIC`
#      `Extreme weather`		:`TRENDING_TOPIC`
#      `Tornados`			:`TRENDING_TOPIC`
#      `Stay at home tomorrow`	:`TRENDING_TOPIC`
#      `Not very pleasant`	:`TRENDING_TOPIC`
# `Party!`			:`DIRECT_MESSAGE` (+ 5 more)
# `Antarctica declared independence`:`TRENDING_TOPIC


# Sorted in ascending order (timestamp)
# 1+ consecutive event with same category -> collapsible 



# keep a streak, the event, started_at,

# streak=(i - started_at)


# for event in events:
    # if prev_event != event:
        # find out streak length 
            # if it crossed the threshold then make it collapsible
            # if it didnt add it directly
    # keep track of streak
        # update started_at
        # prev_event = event

# add events according to steak

# T1 T2 T3
  0  1  2



started_at = -1


for i,event in enumerate(events):
    if prev_event != event:
        ended_at = i-1
        streak_length = (ended_at - started_at) + 1
        if event == 'T' and streak_length >= 2 or event == 'D' and streak_length >= 5:
            events[started_at].collapsible = True
            events[started_at] = []

        
           
