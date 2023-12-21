def max_good_indices(n, permutation):
    # Find the longest increasing subsequence length
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if permutation[i] > permutation[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    max_lis_length = max(lis)

    # If the permutation is already sorted, swap the last two elements
    if max_lis_length == n:
        return n - 1

    # If not, swap the first two elements of the longest increasing subsequence
    return max_lis_length

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        permutation = list(map(int, input().split()))
        result = max_good_indices(n, permutation)
        print(result)

if __name__ == "__main__":
    main()
