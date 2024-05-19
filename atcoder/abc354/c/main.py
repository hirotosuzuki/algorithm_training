#!/usr/bin/env python3
N = int(input())
iAC = []
for idx in range(N):
    a, c = map(int, input().split())
    iAC.append((idx + 1, a, c))
iAC_sorted = sorted(iAC, key=lambda x: x[1])

def make_sequence_ascending_with_indices(sequence):
    from bisect import bisect_left

    if not sequence:
        return [], []

    # dp array to store the indices of the smallest ending value of any increasing subsequence of length i+1
    dp = []
    # To reconstruct the LIS
    lis_indices = []
    # Previous indices to reconstruct the LIS
    prev_index = [-1] * len(sequence)

    for i, num in enumerate(sequence):
        pos = bisect_left([sequence[idx] for idx in dp], num)
        if pos < len(dp):
            dp[pos] = i
        else:
            dp.append(i)
        
        if pos > 0:
            prev_index[i] = dp[pos - 1]

    # Reconstructing the LIS
    lis_length = len(dp)
    lis_sequence = [0] * lis_length
    k = dp[-1]
    for j in range(lis_length - 1, -1, -1):
        lis_sequence[j] = sequence[k]
        lis_indices.append(k)
        k = prev_index[k]
    
    lis_indices.reverse()
    removed_indices = [i for i in range(len(sequence)) if i not in lis_indices]
    
    return lis_sequence, removed_indices

_, removed_indices = make_sequence_ascending_with_indices([x[2] for x in iAC_sorted])
print(_)
answer = [iAC_sorted[i][0] for i in range(N) if i not in removed_indices]
answer.sort()
print(N - len(removed_indices))
print(" ".join(list(map(str, answer))))
