def circles_in_one_group(circles):
    n = len(circles)
    if n <= 1:
        return True

    # Initialize Union-Find structure
    uf = UnionFind(n)

    # Check pairwise overlap and union connected components
    for i in range(n):
        for j in range(i + 1, n):
            if circles_overlap(circles[i], circles[j]):
                uf.union(i, j)

    # Check if all circles are in the same group
    root = uf.find(0)
    for i in range(1, n):
        if uf.find(i) != root:
            return False

    return True
