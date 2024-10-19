


"""
maximise volunteers assigned questions

for question in questions:
    get volunteers that are 'free' and have matching tag
    assign question to volunteer
    mark volunteer as busy
    increment counter
    recur
    backtrack
"""

class Solution:

    


    def solve(self):
        def rec(i=0):
            nonlocal max_questions_assigned
            nonlocal actual_assignments

            if (i == len(questions)): return
            question_id = questions[i]['id']
            for volunteer in volunteers:
                busy_volunteers = question_asssigned.values()
                question_tags = questions[i]['tags']  
                if volunteer['id'] in busy_volunteers: continue
                if not len(set(volunteer['tags']).intersection(set(question_tags))): continue


                # assign question
                question_asssigned[question_id] = volunteer['id']
                assigned_questions=sum([1 if v else 0 for k,v in question_asssigned.items()])
                if assigned_questions > max_questions_assigned:
                    max_questions_assigned = max(assigned_questions,max_questions_assigned)
                    actual_assignments = question_asssigned.copy()
                # recur
                rec(i+1)

                # backtrack
                question_asssigned[question_id] = None

        questions= [
        {'id':"1", 'tags': ["MAC", "VSCODE"]},
        {'id':"2", 'tags': ["PY", "AI"]},
        {'id':"3", 'tags': ["JAVA", "OS"]},
        {'id':"4", 'tags': ["PY", "NW"]}
        ]

        volunteers=[
        {'id': "1", "tags": ["PY","NW"], "name": "A"},
        {'id': "2", "tags": ["AI"], "name": "B"},
        {'id': "3", "tags": ["JAVA","NW"], "name": "C"},
        {'id': "4", "tags": ["JAVA","NW"], "name": "D"}
        ]


        question_asssigned = {q['id']: None for q in questions }
        max_questions_assigned = 0
        actual_assignments = None
        
        for i in range(len(questions)):
            rec(i)

        print(max_questions_assigned)
        print(actual_assignments)

s = Solution()
s.solve()