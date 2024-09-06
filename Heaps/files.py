
def solution(X, B, Z):
    file_size = X
    bytes_downloaded_per_min = B
    last = int(Z)
    file_size_remaining = X - sum(B)
    last_values = B[::-last]
    avg_last_observations = sum(last_values) / len (last_values)
    minutes_remaining = file_size_remaining / avg_last_observations
    return minutes_remaining

print(solution(100,[10,6,6,8],2))


