def cyclic_shift_largest_subsequence(s):
    n = len(s)
    original_s = s
    c = 0

    # Create a dictionary to store the last occurrence index of each character
    last_occurrence = {char: index for index, char in enumerate(s)}

    # While the string is not sorted
    while s != "".join(sorted(s)):
        c += 1

        # Find the lexicographically largest character
        largest_char = max(s)

        # Find the last occurrence of the largest character using the dictionary
        index = last_occurrence[largest_char]

        # Find the lexicographically largest subsequence starting with the largest character
        i = index
        while i < n - 1 and s[i] <= s[i + 1]:
            i += 1

        # Perform a cyclic shift on the largest subsequence
        s = s[:index] + s[i + 1:] + s[index:i + 1]

        # If the string is the same as the original string, it cannot be sorted
        if s == original_s:
            return -1

    return c



 
    
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(cyclic_shift_largest_subsequence(s))