def count_pairs_with_difference(arr, K):
    num_set = set(arr)  # Store elements in a set for O(1) lookups
    count = 0

    for num in arr:
        if (num - K) in num_set:
            count += 1

    return count


# Reading input
T = int(input())  # Number of test cases
for _ in range(T):
    n = int(input())  # Size of array
    arr = list(map(int, input().split()))  # Array elements
    K = int(input())  # Difference key

    print(count_pairs_with_difference(arr, K))
