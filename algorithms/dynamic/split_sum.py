# https://stackoverflow.com/questions/39673898/divide-array-into-k-contiguos-partitions-such-that-sum-of-maximum-partition-is-m
def split_sum(arr, k):
    if k == 1:
        return sum(arr)
    if k == len(arr):
        return max(arr)
    result = 2 ** 32 - 1
    start, end = 0, len(arr)
    for i in range(1, len(arr)):
        lval = sum(arr[start:i])
        rval = split_sum(arr[i:end], k - 1)
        result = min(result, max(lval, rval))
    return result