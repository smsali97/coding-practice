

def is_permutation(s1, s2) -> bool:
    # return s1.sort() == s2.sort() # O (n log n)

    # from collections import Counter

    # Time: O(n), Space: O(n)
    if len(s1) == 0 and len(s2) != 0:
        return False
    if len(s1) != 0 and len(s2) == 0:
        return False
    

    c1 = {}
    for l in s1:
        if l not in c1:
            c1[l] = 1
        else:
            c1[l] += 1
    c2 = {}
    for l in s2:
        if l not in c1.keys():
            return False
        if l not in c2:
            c2[l] = 1
        else:
            c2[l] += 1


    for k in c1.keys():
        if k not in c2 or c1[k] != c2[k]:
            return False
    
    return True
        

print(is_permutation('wow', 'wwo'))
print(is_permutation('wow', 'ww'))
print(is_permutation('wow', 'waw'))
print(is_permutation('wow', 'oow'))