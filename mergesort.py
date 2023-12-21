# Read the number of elements from the standard input
N = int(input())
# Read the array C from the standard input
C = list(map(int, input().split()))
# Initialize two empty lists to store the arrays A and B
A = []
B = []
# Initialize two variables to store the current indices of A and B
i = 0
j = 0
# Initialize a boolean variable to store the possibility of the solution
possible = True
# Loop through all the elements of C
for x in C:
  # If the element is smaller than the last element of A
  if i > 0 and x < A[i - 1]:
    # Append the element to B
    B.append(x)
    # Increment the index of B
    j += 1
  # Else if the element is smaller than the last element of B
  elif j > 0 and x < B[j - 1]:
    # Append the element to A
    A.append(x)
    # Increment the index of A
    i += 1
  # Else if the element is larger than both the last elements of A and B
  elif (i == 0 or x > A[i - 1]) and (j == 0 or x > B[j - 1]):
    # Append the element to either A or B, depending on which one has less elements so far
    if i < j:
      A.append(x)
      i += 1
    else:
      B.append(x)
      j += 1
  # Else, the solution is impossible
  else:
    possible = False
    break
# If the solution is possible and both A and B have the same length
if possible and len(A) == len(B):
  # Print the arrays A and B in two lines
  print(*A)
  print(*B)
# Else, print -1
else:
  print(-1)
