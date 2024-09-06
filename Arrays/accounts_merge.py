class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        # two accounts are the same iff they share a same email

        # adj list
        # connected one email to the rest
        # and mutual emails as well

        # emails <-- nodes
        # map[e1] = e2 , map[e2] = e1 <-- bi-edge

        if not accounts:
            return []
        visited = set()
        email_to_name = {} # e1 --> name
        email_to_email = defaultdict(list) # e1 --> e2


        def dfs(email,emails_of_same_person):
            visited.add(email) # visit this email
            emails_of_same_person.add(email)
            aliases = [alias for alias in email_to_email[email] if alias not in visited]
            for alias in aliases:
                dfs(alias,emails_of_same_person)


        # O(KE)
        for acc in accounts:
            curr_emails = acc[1:]
            name = acc[0]
            if len(curr_emails) < 1: continue  # Check if there are at least one emails in this account
            first_email = curr_emails[0]
            for email in curr_emails:
                email_to_name[email] = name
                email_to_email[first_email].append(email)  # Append to the list
                email_to_email[email].append(first_email)  # Create a bidirectional connection
        result = []
        # O(E Log E)
        for email in email_to_name.keys():
            if email not in visited:
                possible_emails = set()
                name = email_to_name[email]
                dfs(email,possible_emails)
                result.append([name] + sorted(possible_emails))
        return result

