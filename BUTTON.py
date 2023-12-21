# Read the number of test cases from the standard input
T = int(input())
# Loop through all the test cases
for _ in range(T):
  # Read the number of lamps, the initial state, and the final state from the standard input
  N = int(input())
  A = input()
  B = input()
  # Loop through all the lamps except the first and the last
  for i in range(1, N - 1):
    # If the current lamp is different from the desired state
    if A[i] != B[i]:
      # Toggle the state of the adjacent lamps
      A = A[:i - 1] + str(1 - int(A[i - 1])) + A[i:]
      A = A[:i + 1] + str(1 - int(A[i + 1])) + A[i + 2:]
  # Check if the first and the last lamps are equal to the desired state and print the result to the standard output
  print("YES" if A[0] == B[0] and A[N - 1] == B[N - 1] else "NO")

