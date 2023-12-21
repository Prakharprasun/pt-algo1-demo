# Read the number of test cases from the standard input
tc = int(input())
# Loop through all the test cases
for _ in range(tc):
  # Read the number of days, the minimum points, the points for lesson and task from the standard input
  n, P, l, t = map(int, input().split())
  # Initialize a variable to store the number of days Monocarp can rest
  rest = 0
  # Initialize a variable to store the number of tasks unlocked
  tasks = 0
  # Initialize a variable to store the number of tasks completed
  done = 0
  # Initialize a variable to store the number of points earned
  points = 0
  # Loop through all the days
  for day in range(1, n + 1):
    # If the day is a multiple of 7, a new task is unlocked
    if day % 7 == 0:
      tasks += 1
    # If the points earned are enough, Monocarp can rest
    if points >= P:
      rest += 1
    # Else, Monocarp has to study
    else:
      # Monocarp attends a lesson and earns l points
      points += l
      # Monocarp completes up to 2 tasks if possible
      for _ in range(2):
        # If there are tasks unlocked and not completed
        if done < tasks:
          # Monocarp completes a task and earns t points
          points += t
          done += 1
  # Print the number of days Monocarp can rest to the standard output
  print(rest)