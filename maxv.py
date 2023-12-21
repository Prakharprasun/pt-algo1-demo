# Read the number of elements and operations from the standard input
N, M = map(int, input().split())
# Initialize an empty list to store the operations
ops = []
# Loop through all the operations
for _ in range(M):
  # Read the left, right, and value of the operation from the standard input
  L, R, X = map(int, input().split())
  # Append the operation to the list
  ops.append((L, R, X))
# Read the number of queries from the standard input
Q = int(input())
# Loop through all the queries
for _ in range(Q):
  # Read the index, start, and end of the query from the standard input
  K, S, T = map(int, input().split())
  # Initialize a variable to store the answer of the query
  ans = 0
  # Loop through all the operations from start to end
  for i in range(S - 1, T):
    # Get the left, right, and value of the current operation
    L, R, X = ops[i]
    # If the index is within the range of the operation
    if L <= K <= R:
      # Add the value to the answer
      ans += X
  # Print the answer to the standard output
  print(ans)
