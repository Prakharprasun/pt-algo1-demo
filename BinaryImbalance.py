def can_make_zeroes_greater_than_ones(t, testcases):
    results = []
    
    for testcase in testcases:
        n, s = testcase
        # Count the number of zeroes and ones in the string
        count_zeroes = s.count('0')
        count_ones = s.count('1')
        
        # Check if it's already true or can be made true
        if count_zeroes > count_ones or count_zeroes == count_ones:
            results.append("YES")
        else:
            # Check if it's possible to make the number of zeroes greater
            for i in range(1, n):
                if s[i] != s[i-1]:
                    results.append("YES")
                    break
            else:
                results.append("NO")
    
    return results

# Input reading
t = int(input())
testcases = []

for _ in range(t):
    n = int(input())
    s = input().strip()
    testcases.append((n, s))

# Function call and output
results = can_make_zeroes_greater_than_ones(t, testcases)

for result in results:
    print(result)


